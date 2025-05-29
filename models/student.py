# models/student.py

from models.studiengang import Studiengang

class Student:
    """
    Repräsentiert einen Studenten oder eine Studentin.

    Attribute:
    ----------
    name : str
        Der vollständige Name.
    matrikelnummer : str
        Die Matrikelnummer des Studierenden.
    studiengang : Studiengang
        Der zugeordnete Studiengang.
    """

    def __init__(self, name: str, matrikelnummer: str, studiengang: Studiengang):
        self.name = name
        self.matrikelnummer = matrikelnummer
        self.studiengang = studiengang

    def get_studienfortschritt(self) -> float:
        """
        Gibt den Studienfortschritt in Prozent zurück.
        """
        return self.studiengang.berechne_fortschritt()

    def get_notendurchschnitt(self) -> float:
        """
        Berechnet den Durchschnitt aller Noten abgeschlossener Module.
        Gibt 0.0 zurück, wenn keine Noten vorhanden sind.
        """
        noten = []
        for semester in self.studiengang.semester:
            for modul in semester.module:
                if modul.abgeschlossen and modul.note is not None:
                    noten.append(modul.note)

        return round(sum(noten) / len(noten), 2) if noten else 0.0

    def display_info(self):
        """
        Gibt die Informationen des Studierenden aus.
        """
        print(f"Name: {self.name}")
        print(f"Matrikelnummer: {self.matrikelnummer}")
