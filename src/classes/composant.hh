#pragma once

class Composant
{
protected:
    int id;
    int typeComp;

public:
    Composant(int idComp, int typeComp) : id(idComp), typeComp(typeComp) {}

    virtual int Fonction() = 0;

    virtual ~Composant() = default;
};
