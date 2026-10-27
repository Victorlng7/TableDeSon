#pragma once
#include <Arduino.h>
#include "composant.hh"

class Potentiometre : public Composant
{
protected:
    uint8_t pin;

public:
    Potentiometre(uint8_t broche)
        : Composant(0, 1), pin(broche)
    {
    }

    int Fonction() override;
};
