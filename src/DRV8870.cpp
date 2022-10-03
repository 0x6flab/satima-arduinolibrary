#include "DRV8870.h"
#include "Arduino.h"

DRV8870::DRV8870(int motor_pin_1, int motor_pin_2)
{
    pinMode(motor_pin_1, OUTPUT);
    pinMode(motor_pin_2, OUTPUT);
    this->_motor_count = 1;
}
DRV8870::DRV8870(int motor_pin_1, int motor_pin_2, int motor_pin_3, int motor_pin_4)
{
    pinMode(motor_pin_1, OUTPUT);
    pinMode(motor_pin_2, OUTPUT);
    pinMode(motor_pin_3, OUTPUT);
    pinMode(motor_pin_4, OUTPUT);
    this->_motor_count = 2;
}
void DRV8870::setMaxSpeed(int max_speed = 255)
{
    this->max_speed = max_speed;
}
void DRV8870::setSpeed(int motor_speed, int direction = CLOCKWISE)
{
    switch (this->_motor_count)
    {
    case 1:
        switch (direction)
        {
        case CLOCKWISE:
            analogWrite(_motor_pin_1, motor_speed);
            analogWrite(_motor_pin_1, 0);
            break;
        case COUNTERCLOCKWISE:
            analogWrite(_motor_pin_1, 0);
            analogWrite(_motor_pin_1, motor_speed);
            break;
        default:
            break;
        }
        break;
    case 2:
        switch (direction)
        {
        case CLOCKWISE:
            analogWrite(_motor_pin_1, motor_speed);
            analogWrite(_motor_pin_2, 0);
            analogWrite(_motor_pin_3, motor_speed);
            analogWrite(_motor_pin_4, 0);
            break;
        case COUNTERCLOCKWISE:
            analogWrite(_motor_pin_1, 0);
            analogWrite(_motor_pin_2, motor_speed);
            analogWrite(_motor_pin_3, 0);
            analogWrite(_motor_pin_4, motor_speed);
            break;
        default:
            break;
        }
        break;

    default:
        break;
    }
}
void DRV8870::brake(int mode = COAST)
{
    if (mode == COAST)
    {
        switch (this->_motor_count)
        {
        case 1:
            digitalWrite(_motor_pin_1, LOW);
            digitalWrite(_motor_pin_2, LOW);
            break;
        case 2:
            digitalWrite(_motor_pin_1, LOW);
            digitalWrite(_motor_pin_2, LOW);
            digitalWrite(_motor_pin_3, LOW);
            digitalWrite(_motor_pin_4, LOW);
            break;
        default:
            break;
        }
    }
    else if (mode == BRAKE)
    {
        switch (this->_motor_count)
        {
        case 1:
            digitalWrite(_motor_pin_1, HIGH);
            digitalWrite(_motor_pin_2, HIGH);
            break;
        case 2:
            digitalWrite(_motor_pin_1, HIGH);
            digitalWrite(_motor_pin_2, HIGH);
            digitalWrite(_motor_pin_3, HIGH);
            digitalWrite(_motor_pin_4, HIGH);
            break;
        default:
            break;
        }
    }
}
int DRV8870::version(void)
{
    return _version;
}