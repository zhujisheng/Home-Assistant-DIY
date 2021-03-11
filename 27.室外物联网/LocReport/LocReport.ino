#include "SIM7000.h"
#include <SoftwareSerial.h>
#define RXD2 10
#define TXD2 11

//你需要修改以下信息
#define NetworkAPN "cmnbiot3"
#define ServerIP "54.255.233.63"
#define ServerPort 5055
#define DeviceID 123456

SoftwareSerial mySS = SoftwareSerial(RXD2, TXD2);
SIM7000    sim7000;

void setup() {
  Serial.begin(115200);
  mySS.begin(19200);

  //连接到sim7000
  if (sim7000.begin(mySS))
    Serial.println("Connected to Sim7000 ok.");
  else{
    Serial.println("Couldn't connect to Sim7000 module!");
    while(1);
  }

  //探测sim卡已插入
  if(sim7000.check_send_cmd("AT+CPIN?\r\n","CPIN: READY"))
    Serial.println("SIM card READY.");
  else{
    Serial.println("SIM card ERROR, Check if you have insert SIM card and restart SIM7000!");
    while(1);
  }

  //选择LTE，NB-IOT，打开扰码
  if(sim7000.check_send_cmd("AT+CNMP=38\r\n","OK"))
    Serial.println("Select LTE OK.");
  else{
    Serial.println("Select LTE, return error!");
    while(1);
  }
  if(sim7000.check_send_cmd("AT+CMNB=2\r\n","OK"))
    Serial.println("Select NB-IOT OK.");
  else{
    Serial.println("Select NB-IOT, return error!");
    while(1);
  }
  if(sim7000.check_send_cmd("AT+NBSC=1\r\n","OK"))
    Serial.println("Enable the scrambling feature OK.");
  else{
    Serial.println("Enable the scrambling feature, return error!");
    while(1);
  }

  //获得可用的APN
  sim7000.check_send_cmd("AT+CGNAPN\r\n","OK");

  //设置APN，连接网络
  char command[100];
  sprintf(command, "AT+CSTT=\"%s\"\r\n",NetworkAPN);
  if(sim7000.check_send_cmd(command,"OK"))
    Serial.println("Set APN OK.");
  else{
    Serial.println("Set APN, not return OK!");
  }

  if(sim7000.check_send_cmd("AT+CIICR\r\n","OK"))
    Serial.println("CIICR OK.");
  else
    Serial.println("Set CIICR, not return OK!");

  //打开卫星定位电源
  if(sim7000.check_send_cmd("AT+CGNSPWR=1\r\n","OK"))
    Serial.println("CGNSPWR OK.");
  else{
    Serial.println("CGNSPWR, return error!");
    while(1);
  }
}

void loop() {
  char GNSSBuffer[150];
  char command[200];
  char *p, *lat, *lon, *datetime;

  // 获得时间与经纬度
  sim7000.sendCmd("AT+CGNSINF\r\n");
  sim7000.readBuffer(GNSSBuffer, 150);
  p = strstr(GNSSBuffer, ",");
  p = strstr(p+1, ",");
  datetime = p+1;
  p = strstr(p+1, ",");
  *p = NULL;
  lat = p+1;
  p = strstr(p+1, ",");
  *p = NULL;
  lon = p+1;
  p = strstr(p+1, ",");
  *p = NULL;

  Serial.print("Datetime: ");
  Serial.println(datetime);
  Serial.print("Latitude: ");
  Serial.println(lat);
  Serial.print("Longitude: ");
  Serial.println(lon);

  sim7000.check_send_cmd("AT+CIFSR\r\n", "OK");
  // 连接traccar服务器，发送数据
  if(strlen(datetime)>0){
    Serial.println("Connect to server...");
    sprintf(command, "AT+CIPSTART=\"TCP\",\"%s\",%d\r\n", ServerIP, ServerPort);
    sim7000.check_send_cmd(command,"OK", 20000, 10000);

    if(sim7000.check_send_cmd("AT+CIPSTATUS\r\n","CONNECT OK")){
      sprintf(command, "GET /?id=%ld&lat=%s&lon=%s HTTP/1.1\r\n\r\n", DeviceID, lat, lon);
      sim7000.check_send_cmd("AT+CIPSEND\r\n", ">");
      sim7000.sendCmd(command);
      sim7000.check_send_cmd("\x1a", "SEND OK", 20000, 10000);
      sim7000.check_send_cmd("AT+CIPCLOSE\r\n", "OK", 20000, 10000);
    }
  }
  delay(5000);
}
