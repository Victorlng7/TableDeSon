#include "classes/composant.hh"
#include "classes/pottentiometre.hh"
#include "classes/bouton.hh"

// creation des objet
Bouton boutonEnceinte(3);
Bouton boutonCasque(4);
Bouton boutonPreviousTrack(5);
Bouton boutonPlayPause(6);
Bouton boutonNextTrack(7);

Potentiometre master(A0);
Potentiometre app1(A1);
Potentiometre app2(A2);
Potentiometre app3(A3);
Potentiometre app4(A4);

// tableau d'objt
Composant *composants[10] = {&boutonEnceinte, &boutonCasque, &boutonPreviousTrack, &boutonPlayPause, &boutonNextTrack, &master, &app1, &app2, &app3, &app4};

// tableau de différence entre les input de valeurs
int anciennesValeurs[10] = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
// --------------------

void setup()
{
    Serial.begin(9600);

    // securité pullup
    pinMode(3, INPUT_PULLUP);
    pinMode(4, INPUT_PULLUP);
    pinMode(5, INPUT_PULLUP);
    pinMode(6, INPUT_PULLUP);
    pinMode(7, INPUT_PULLUP);
}

void loop()
{
    for (int i = 0; i < 10; i++)
    {
        int valeur = composants[i]->Fonction();

        // calcule de l'écart avec l'ancienne valeur
        int difference = abs(valeur - anciennesValeurs[i]);

        // si diférence on serial.print
        if ((i < 5 && difference > 0) || (i >= 5 && difference > 2))
        {
            Serial.print(i);
            Serial.print("/");
            Serial.println(valeur);

            anciennesValeurs[i] = valeur;
        }
    }

    delay(10);
}