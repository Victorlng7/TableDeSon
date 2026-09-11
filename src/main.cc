#include <Arduino.h>
#include "classes/composant.hh"
#include "classes/pottentiometre.hh"

// Adafruit_LiquidCrystal lcd(16x2);

void setup()
{
    // bouton
    pinMode(12, INPUT);
    pinMode(12, INPUT);
    pinMode(12, INPUT);
    pinMode(12, INPUT);
    pinMode(12, INPUT);

    // pottards
    pinMode(A0, INPUT);
    pinMode(A1, INPUT);
    pinMode(A2, INPUT);
    pinMode(A3, INPUT);
    pinMode(A4, INPUT);
}

int main()
{
    Composant *P1 = Potentiometre("A0");
}