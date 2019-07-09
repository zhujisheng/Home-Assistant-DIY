#include "SIM7000.h"

bool  SIM7000::begin(Stream &port)
{
  mySerial = &port;

  int16_t timeout = 7000;
  while (timeout > 0) {
    while (mySerial->available()) mySerial->read();
    if (check_send_cmd("AT\r\n","OK"))
      return true;
    delay(500);
    timeout-=500;
  }
  return false;
}

bool  SIM7000::checkSIMStatus(void)
{
    int count = 0;
    while(count < 3){
        if(check_send_cmd("AT\r\n","OK")){
            break;
        }else{
            count++;
            delay(300);
        }
    }
    if(count == 3){
        return false;
    }
    count = 0;
    while(count < 3){
        if(check_send_cmd("AT+CPIN?\r\n","READY")){
            break;
        }else{
            count++;
            delay(300);
        }
    }
    if(count == 3){
        return false;
    }
    return true;
}

bool  SIM7000::check_send_cmd(const char* cmd, const char* resp, unsigned int timeout, unsigned int chartimeout)
{
    char SIMbuffer[100];
    sendCmd(cmd);
    readBuffer(SIMbuffer,100, timeout, chartimeout);
    if(NULL != strstr(SIMbuffer,resp)){
        return  true;
    }else{
        return  false;
    }
}

void SIM7000::sendCmd(const char* cmd)
{
    mySerial->write(cmd);
    Serial.println("================>>>>>>");
    Serial.print("SendCommand: ");
    Serial.print(cmd);
}

int SIM7000::readBuffer(char *buffer, int count, unsigned int timeout, unsigned int chartimeout)
{
    int i = 0;
    unsigned long timerStart, prevChar;
    timerStart = millis();
    prevChar = 0;
    while(1){
        while(mySerial->available()>0){
            buffer[i++] = mySerial->read();
            prevChar = millis();
            if(i >= count){
                buffer[i] = '\0';
                Serial.println("<<<<<<<================");
                Serial.println(buffer);
                return i;
            }
        }
        if(timeout){
            if((unsigned long) (millis() - timerStart) > timeout){
                break;
            }
        }
        if(((unsigned long) (millis() - prevChar) > chartimeout) && (prevChar != 0)){
            break;
        }
    }
    buffer[i] = '\0';
    Serial.println("<<<<<<<================");
    Serial.println(buffer);
    return i;
}
