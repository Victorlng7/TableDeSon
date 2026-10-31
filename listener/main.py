import serial
import time

# Configuration
PORT = 'COM5' # A changer selon le port arduino
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
    valeur = int(valeur)
    if not 0 <= valeur <= 1023:
        raise ValueError("La valeur du potentiomètre doit être entre 0 et 1023")
    return valeur * 100 // 1023


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
        composant, valeur = message.split(":", 1)
        composant = composant.strip()
        valeur = valeur.strip()

        # Boutons : format "3 : appuye" ou "3 : relache"
        if composant.isdigit():
            bouton = int(composant)

            if valeur == "appuye":
                if bouton == 3:
                    set_enceinte()
                elif bouton == 4:
                    set_casque()
                elif bouton == 5:
                    previous_track()
                elif bouton == 6:
                    play_pause()
                elif bouton == 7:
                    next_track()

        # Potentiomètres : format "A0 : 512"
        elif composant in ("A0", "A1", "A2", "A3", "A4"):
            valeur = int(valeur)

            if composant == "A1":
                set_app1_volume("Discord", valeur)
            elif composant == "A2":
                set_app2_volume("Chrome", valeur)
            elif composant == "A3":
                set_app3_volume("CS", valeur)
            elif composant == "A4":
                set_app4_volume("RL", valeur)
            elif composant == "A0":
                set_master_volume(valeur)

        else:
            print(f"Message inconnu : {message}")

    except (ValueError, TypeError):
        print(f"Message invalide : {message}")

# Boucle principale
def main():
    print(f"Lancement de l'écoute de la carte arduino (port :{PORT})...")
    try:
        # Connexion
        with serial.Serial(PORT, BAUD_RATE, timeout=None) as arduino:
            # L'ouverture du port redémarre souvent l'Arduino; attendre son démarrage.
            time.sleep(2)
            arduino.reset_input_buffer()
            while True:
                ligne = arduino.readline().decode("utf-8", errors="ignore").strip()

                if ligne:
                    traiter_message(ligne)                
    
    # Message d'erreur
    except serial.SerialException as erreur:
        print(f"Erreur : Impossible de se connecter au port {PORT} : {erreur}")

if __name__ == "__main__":
    main()