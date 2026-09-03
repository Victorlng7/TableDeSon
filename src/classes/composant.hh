#pragma once

class Composant
{

protected:
    int idComp;

    int typeComp;

public:
    Composant(int idComp, int typeComp);

    virtual int Fonction() = 0;
};