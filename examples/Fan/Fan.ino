#include <DRV8870.h>

DRV8870 mymotor(8, 9);

void setup()
{
    mymotor.setMaxSpeed(255);
}

void loop()
{
    mymotor.setSpeed(255, CLOCKWISE);
    delay(50000);
}