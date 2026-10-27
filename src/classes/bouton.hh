#pragma once
#include "composant.hh"

class Bouton : public Composant
{
protected:
    uint8_t pin;

public:
    Bouton(uint8_t broche)
        : Composant(0, 1), pin(broche)
    {
    }

    int Fonction() override;
};