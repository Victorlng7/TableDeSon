#include <Arduino.h>

void setup()
{
    Serial.begin(115200);
    while (!Serial)
        ;
}

// 1 seul fader

// void loop()
// {
//     int valA0 = analogRead(A0);

//     Serial.print("A0:");

//     Serial.println(valA0);

//     delay(100);
// }

// 5 faders

void loop()
{
    int valA0 = analogRead(A0);
    int valA1 = analogRead(A1);
    int valA2 = analogRead(A2);
    int valA3 = analogRead(A3);
    int valA4 = analogRead(A4);

    Serial.print("A0:");
    Serial.print(valA0);
    Serial.print(" | A1:");
    Serial.print(valA1);
    Serial.print(" | A2:");
    Serial.print(valA2);
    Serial.print(" | A3:");
    Serial.print(valA3);
    Serial.print(" | A4:");
    Serial.println(valA4);

    delay(100);
}