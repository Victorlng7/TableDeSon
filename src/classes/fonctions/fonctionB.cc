#include <Arduino.h>
#include "../bouton.hh"

int Bouton::Fonction()
{
    if (digitalRead(this->pin) == LOW)
    {
        return 1;
    }

    return 0;
};