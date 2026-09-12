#include <Arduino.h>
#include "../pottentiometre.hh"

int Potentiometre::Fonction()
{
    int valeurPotar = analogRead(this->pin);

    return valeurPotar;

    delay(500);
};