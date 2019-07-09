#ifndef __SIM7000_H__
#define __SIM7000_H__

#include <Arduino.h>
#include <SoftwareSerial.h>
#define DEFAULT_TIMEOUT              5000    //miliseconds
#define DEFAULT_INTERCHAR_TIMEOUT    1500    //miliseconds

class SIM7000
{
public:
    bool begin(Stream &port);
    void sendCmd(const char* cmd);
    int readBuffer(char *buffer, int count, unsigned int timeout = DEFAULT_TIMEOUT, unsigned int chartimeout = DEFAULT_INTERCHAR_TIMEOUT);
    bool check_send_cmd(const char* cmd, const char* resp, unsigned int timeout = DEFAULT_TIMEOUT, unsigned int chartimeout = DEFAULT_INTERCHAR_TIMEOUT);
private:
    SoftwareSerial* mySerial;
 };

#endif
