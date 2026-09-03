#pragma once
#include "composant.hh"

class Potentiometre : public Composant
{
private:
    int pin;

public:
    Potentiometre(int broche);
    int Fonction()
    {
        int valeurPotar = analogRead(12);

        // Mettre la valeur de valeurPotar dans x volume (mélangeur volume)
    };
};