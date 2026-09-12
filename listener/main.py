import serial
import time

from arduino.app_utlis import App

# Configuration
PORT = '/dev/ttyUSB0' # A changer selon le port arduino
BAUD_RATE = 9600

# Action Bouton
def play_pause():
    print("Action : Lecture / Pause de la musique")

def next_track ():
    print("Action : Prochaine piste")

def previous_track ():
    print("Action : piste précédente")

def set_casque ():
    print("Action : Définition de la sortie audio au casque")

def set_enceinte ():
    print("Action : Définition de la sortie audio aux enceintes")


#Convertir en pourcentage
def convertir_pourcentage(valeur):
    return (int (int (valeur)/1023) * 100)


#Fader
def set_master_volume(valeur_brute):
    pourcentage = convertir_pourcentage(valeur_brute) 
    print(f"Volume Master réglé à : {pourcentage}%")

def set_app1_volume(app_name, valeur_brute):
    pourcentage = convertir_pourcentage(valeur_brute) 
    print(f"Volume {app_name} réglé sur {pourcentage}")

def set_app2_volume(app_name, valeur_brute):
    pourcentage = convertir_pourcentage(valeur_brute) 
    print(f"Volume {app_name} réglé sur {pourcentage}")

def set_app3_volume(app_name, valeur_brute):
    pourcentage = convertir_pourcentage(valeur_brute) 
    print(f"Volume {app_name} réglé sur {pourcentage}")

def set_app4_volume(app_name, valeur_brute):
    pourcentage = convertir_pourcentage(valeur_brute) 
    print(f"Volume {app_name} réglé sur {pourcentage}")

# Routage
def traiter_message(message):
    try:
        composant, valeur = message.split(":")
        
        # Routage des Boutons
        if composant == "BTN1" and valeur == "1":
            play_pause()
        elif composant == "BTN2" and valeur == "1":
            next_track()
        elif composant == "BTN3" and valeur == "1":
            previous_track()
        elif composant == "BTN4" and valeur == "1":
            set_casque()
        elif composant == "BTN5" and valeur == "1":
            set_enceinte()
            
        # Routage des Faders
        elif composant == "FADER1":
            set_master_volume(valeur)
        elif composant == "FADER2":
            set_app1_volume("Discord", valeur)
        elif composant == "FADER3":
            set_app2_volume("Chrome", valeur)
        elif composant == "FADER4":
            set_app3_volume("CS", valeur)
        elif composant == "FADER5":
            set_app4_volume("RL", valeur)
            
    except ValueError:
        pass

# Boucle principale
def main():
    print(f"Lancement de l'écoute de la carte arduino (port :{PORT})...")
    try:
        # Connexion
        with serial.Serial(PORT, BAUD_RATE, timeout=0.1) as arduino:
            while True:
                if arduino.in_waiting > 0:
                    # Encodage UTF-8 du l'input arduino
                    ligne = arduino.readline().decode('utf-8').strip()
                    if ligne:
                        traiter_message(ligne)
                        
                # Pause pour pas surcharger le CPU
                time.sleep(0.1) 
    
    # Message d'erreur
    except serial.SerialException:
        print(f"Erreur : Impossible de se connecter au port {PORT}.")

if __name__ == "__main__":
    main()