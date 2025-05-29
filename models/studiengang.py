# models/studiengang.py

from models.semester import Semester
from typing import List, Optional

class Studiengang:
    """
    Repräsentiert einen Studiengang mit mehreren Semestern.

    Attribute:
    ----------
    name : str
        Name des Studiengangs.
    regelstudienzeit : int
        Regelstudienzeit in Semestern.
    semester : List[Semester]
        Liste der Semester dieses Studiengangs.
    """

    def __init__(self, name: str, regelstudienzeit: int):
        self.name = name
        self.regelstudienzeit = regelstudienzeit
        self.semester: List[Semester] = []

    def add_semester(self, semester: Semester):
        """
        Fügt ein Semester zum Studiengang hinzu.
        """
        self.semester.append(semester)

    def berechne_fortschritt(self) -> float:
        """
        Berechnet den Fortschritt basierend auf abgeschlossenen Modulen.
        Rückgabe als Prozentwert.
        """
        alle_module = [modul for sem in self.semester for modul in sem.module]
        abgeschlossen = [modul for modul in alle_module if modul.abgeschlossen]
        if not alle_module:
            return 0.0
        return round((len(abgeschlossen) / len(alle_module)) * 100, 2)

    def ist_regelstudienzeit_eingehalten(self) -> bool:
        """
        Prüft, ob die Anzahl der belegten Semester innerhalb der Regelstudienzeit liegt.
        """
        return len(self.semester) <= self.regelstudienzeit

    def __str__(self):
        return f"{self.name} ({len(self.semester)} Semester)"
