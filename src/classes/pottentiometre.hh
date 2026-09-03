#pragma once
#include "composant.hh"

class Potentiometre : public Composant
{
protected:
    int pin;

public:
    Potentiometre(int broche);

    int Fonction(this->pin);
};