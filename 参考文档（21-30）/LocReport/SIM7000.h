#ifndef __SIM7000_H__
#define __SIM7000_H__

#include <Arduino.h>
#include <SoftwareSerial.h>
#define DEFAULT_TIMEOUT              5000    //miliseconds
#define DEFAULT_INTERCHAR_TIMEOUT    1500    //miliseconds

class SIM7000
{
public:
    bool check_send_cmd(const char* cmd, const char* resp, unsigned int timeout = DEFAULT_TIMEOUT, unsigned int chartimeout = DEFAULT_INTERCHAR_TIMEOUT);
    void sendCmd(const char* cmd);
    int readBuffer(char *buffer, int count, unsigned int timeout = DEFAULT_TIMEOUT, unsigned int chartimeout = DEFAULT_INTERCHAR_TIMEOUT);
    bool setBaudRate(long rate);
    bool checkSIMStatus(void);
    bool begin(Stream &port);
private:
    char     latitude[8];
    char     longitude[8];
    SoftwareSerial* mySerial;
 };

#endif
