#include <Arduino.h>

const int boutons[] = {7, 8, 9, 10, 11};
const int potentiometres[] = {A0, A1, A2, A3, A4};

int anciennesValeursBoutons[] = {HIGH, HIGH, HIGH, HIGH, HIGH};
int anciennesValeursPotars[] = {-1, -1, -1, -1, -1};

void setup()
{
    Serial.begin(9600);

    for (int i = 0; i < 5; i++)
    {
        pinMode(boutons[i], INPUT_PULLUP);
    }
}

void loop()
{
    // Boutons
    for (int i = 0; i < 5; i++)
    {
        int valeur = digitalRead(boutons[i]);

        if (valeur != anciennesValeursBoutons[i])
        {
            Serial.print(boutons[i]);
            Serial.print(" : ");
            Serial.println(valeur == LOW ? "appuye" : "relache");

            anciennesValeursBoutons[i] = valeur;
        }
    }

    // Potentiometres
    for (int i = 0; i < 5; i++)
    {
        int valeur = analogRead(potentiometres[i]);

        if (abs(valeur - anciennesValeursPotars[i]) > 2)
        {
            Serial.print("A");
            Serial.print(i);
            Serial.print(" : ");
            Serial.println(valeur);

            anciennesValeursPotars[i] = valeur;
        }
    }

    delay(10);
}
