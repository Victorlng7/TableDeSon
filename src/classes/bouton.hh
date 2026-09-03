#pragma once
#include "composant.hh"

class Bouton : public Composant
{
protected:
    int pin;

public:
    Bouton(int broche);

    int Fonction(this->pin);
};