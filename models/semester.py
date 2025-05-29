# models/semester.py

from models.modul import Modul
from typing import List, Optional

class Semester:
    """
    Repräsentiert ein Semester im Studiengang.

    Attribute:
    ----------
    semester_nr : int
        Die Nummer des Semesters (z. B. 1 für erstes Semester).
    module : List[Modul]
        Liste der Module, die in diesem Semester enthalten sind.
    """

    def __init__(self, semester_nr: int):
        self.semester_nr = semester_nr
        self.module: List[Modul] = []

    def berechne_durchschnitt(self) -> Optional[float]:
        """
        Berechnet die Durchschnittsnote der abgeschlossenen Module in diesem Semester.
        Gibt None zurück, wenn keine Module abgeschlossen wurden.
        """
        noten = [modul.note for modul in self.module if modul.abgeschlossen and modul.note is not None]
        return round(sum(noten) / len(noten), 2) if noten else None

    def get_abgeschlossen_status(self) -> bool:
        """
        Gibt zurück, ob alle Module in diesem Semester abgeschlossen wurden.
        """
        return all(modul.abgeschlossen for modul in self.module)

    def __str__(self):
        return f"Semester {self.semester_nr} mit {len(self.module)} Modulen"
