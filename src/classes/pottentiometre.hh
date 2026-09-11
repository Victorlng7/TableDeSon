#pragma once
#include "composant.hh"

class Potentiometre : public Composant
{
protected:
    String pin;

public:
    Potentiometre(String broche)
        : Composant(0, 1), pin(broche)
    {
    }

    int Fonction() override;
};
