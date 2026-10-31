
import serial
import time

from windows_audio import WindowsAudio

# Configuration
PORT = 'COM5'
BAUD_RATE = 9600

# Initialisation du mixeur Windows
audio = WindowsAudio()


# Actions boutons
def play_pause():
    print("Action : Lecture / Pause de la musique")


def next_track():
    print("Action : Prochaine piste")


def previous_track():
    print("Action : Piste précédente")


def set_casque():
    audio.set_output("Casque")


def set_enceinte():
    audio.set_output("Haut-parleurs (High")


# Convertir en pourcentage
def convertir_pourcentage(valeur):
    valeur = int(valeur)

    if not 0 <= valeur <= 1023:
        raise ValueError("Valeur du potentiomètre invalide")

    return 100 - (valeur * 100 // 1023)
#pottards a l'envers donc changement de 0% -> 100%...


# Faders
def set_master_volume(valeur_brute):
    pourcentage = convertir_pourcentage(valeur_brute)
    audio.set_master_volume(pourcentage)


def set_app1_volume(valeur_brute):
    pourcentage = convertir_pourcentage(valeur_brute)
    audio.set_app_volume("chrome.exe", pourcentage)


def set_app2_volume(valeur_brute):
    pourcentage = convertir_pourcentage(valeur_brute)
    audio.set_app_volume("Discord.exe", pourcentage)


def set_app3_volume(valeur_brute):
    pourcentage = convertir_pourcentage(valeur_brute)
    audio.set_app_volume("cs2.exe", pourcentage)


def set_app4_volume(valeur_brute):
    pourcentage = convertir_pourcentage(valeur_brute)
    audio.set_app_volume("RocketLeague.exe", pourcentage)


# Routage
def traiter_message(message):
    try:
        composant, valeur = message.split(":", 1)
        composant = composant.strip()
        valeur = valeur.strip()

        # Boutons
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

        # Potentiomètres
        elif composant in ("A0", "A1", "A2", "A3", "A4"):
            valeur = int(valeur)

            if composant == "A0":
                set_master_volume(valeur)
            elif composant == "A1":
                set_app1_volume(valeur)
            elif composant == "A2":
                set_app2_volume(valeur)
            elif composant == "A3":
                set_app3_volume(valeur)
            elif composant == "A4":
                set_app4_volume(valeur)

        else:
            print(f"Message inconnu : {message}")

    except (ValueError, TypeError) as erreur:
        print(f"Message invalide : {message} ({erreur})")


# Boucle principale
def main():
    print(f"Lancement de l'écoute Arduino (port : {PORT})...")

    try:
        with serial.Serial(PORT, BAUD_RATE, timeout=None) as arduino:

            time.sleep(2)
            arduino.reset_input_buffer()

            print("Arduino connecté !")
            print("Sorties audio disponibles :")

            for sortie in audio.get_outputs():
                print(f"- {sortie}")

            while True:
                ligne = arduino.readline().decode(
                    "utf-8", errors="ignore"
                ).strip()

                if ligne:
                    traiter_message(ligne)

    except serial.SerialException as erreur:
        print(f"Erreur de connexion Arduino : {erreur}")


if __name__ == "__main__":
    main()
