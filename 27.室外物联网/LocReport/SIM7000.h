#ifndef __SIM7000_H__
#define __SIM7000_H__

#include <Arduino.h>
#include <SoftwareSerial.h>
#define DEFAULT_TIMEOUT              5000    //miliseconds
#define DEFAULT_INTERCHAR_TIMEOUT    1500    //miliseconds

class SIM7000
{
public:
    //初始化
    bool begin(Stream &port);

    //向sim7000模块发送命令
    void sendCmd(const char* cmd);

    //读收到的信息
    int readBuffer(char *buffer, int count, unsigned int timeout = DEFAULT_TIMEOUT, unsigned int chartimeout = DEFAULT_INTERCHAR_TIMEOUT);

    //发送命令，并接收返回，判断返回内容是否包含字符串resp
    bool check_send_cmd(const char* cmd, const char* resp, unsigned int timeout = DEFAULT_TIMEOUT, unsigned int chartimeout = DEFAULT_INTERCHAR_TIMEOUT);
private:
    SoftwareSerial* mySerial;
 };

#endif
