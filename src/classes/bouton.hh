#pragma once
#include "composant.hh"

class Bouton : public Composant
{
protected:
    String pin;

public:
    Bouton(String broche)
        : Composant(0, 1), pin(broche)
    {
        pinMode(pin, INPUT);
    }

    int Fonction(this->pin);
};