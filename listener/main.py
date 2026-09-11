import serial
import time

# Configuration
PORT = '/dev/ttyUSB0' # A changer selon le port arduino
BAUD_RATE = 9600

# Action Bouton
def play_pause():
    print("Action : Lecture / Pause de la musique")

def mute_micro():
    print("Action : Micro mute (Silence)")

# Fader
def set_master_volume(valeur_brute):
    pourcentage = int((int(valeur_brute) / 1023) * 100) # Valeur int --> valeur en pourcentage
    print(f"Volume Master réglé à : {pourcentage}%")

def set_app_volume(app_name, valeur_brute):
    print(f"Volume {app_name} réglé sur {valeur_brute}")

# Routage
def traiter_message(message):
    try:
        composant, valeur = message.split(":")
        
        # Routage des Boutons
        if composant == "BTN1" and valeur == "1":
            play_pause()
        elif composant == "BTN2" and valeur == "1":
            mute_micro()
            
        # Routage des Faders
        elif composant == "FADER1":
            set_master_volume(valeur)
        elif composant == "FADER2":
            set_app_volume("Discord", valeur)
            
    except ValueError:
        pass

# Boucle principale
def main():
    print(f"Lancement de l'écoute sur le port {PORT}...")
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