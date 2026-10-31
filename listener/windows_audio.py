
from pycaw.pycaw import AudioUtilities
from pycaw.constants import DEVICE_STATE, EDataFlow


class WindowsAudio:

    def __init__(self):
        self.outputs = AudioUtilities.GetAllDevices(
            data_flow=EDataFlow.eRender.value,
            device_state=DEVICE_STATE.ACTIVE.value
        )

    # Volume général
    def set_master_volume(self, pourcentage):
        device = AudioUtilities.GetSpeakers()
        device.volume_percent = pourcentage

    # Volume d'une application
    def set_app_volume(self, app_name, pourcentage):
        sessions = AudioUtilities.GetAllSessions()

        for session in sessions:
            if session.Process:
                if session.Process.name().lower() == app_name.lower():
                    session.SimpleAudioVolume.SetMasterVolume(
                        pourcentage / 100, None
                    )

    # Changer la sortie audio par défaut
    def set_output(self, nom):
        for device in self.outputs:
            if nom.lower() in device.FriendlyName.lower():
                AudioUtilities.SetDefaultDevice(device.id)
                print(f"Sortie audio sélectionnée : {device.FriendlyName}")
                return

        print(f"Sortie audio introuvable : {nom}")

    # Afficher les sorties disponibles
    def get_outputs(self):
        return [device.FriendlyName for device in self.outputs]

    # Afficher la sortie actuelle
    def get_current_output(self):
        return AudioUtilities.GetSpeakers().FriendlyName
