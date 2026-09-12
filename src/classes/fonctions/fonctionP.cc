#include <Arduino.h>
#include "../pottentiometre.hh"

int Potentiometre::Fonction()
{
    int valeurPotar = analogRead(this->pin);

    Serial.println(valeurPotar);

    delay(500);
};