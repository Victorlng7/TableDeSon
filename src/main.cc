#include "classes/composant.hh"
#include "classes/pottentiometre.hh"
#include "classes/bouton.hh"

// Adafruit_LiquidCrystal lcd(16x2);

void setup()
{
    Serial.begin(9600);

    Bouton boutonEnceinte("2");
    Bouton boutonCasque("3");
    Bouton boutonPreviousTrack("4");
    Bouton boutonPlayPause("5");
    Bouton boutonNextTrack("6");

    Potentiometre master("A0");
    Potentiometre app1("A1");
    Potentiometre app2("A2");
    Potentiometre app3("A3");
    Potentiometre app4("A4");

    Composant *composants[10] = {&boutonEnceinte, &boutonCasque, &boutonPreviousTrack, &boutonPlayPause, &boutonNextTrack, &master, &app1, &app2, &app3, &app4};
}

int loop()
{
    for (int i = 0; i < 2; i++)
    {
        int valeur = composants[i]->Fonction();

        if (valeur > 0)
        {
        }
    }

    delay(50);
}