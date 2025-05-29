# models/modul.py

class Modul:
    """
    Repräsentiert ein Studienmodul innerhalb eines Semesters.

    Attribute:
    ----------
    name : str
        Name des Moduls.
    note : float, optional
        Note des Moduls (z. B. 1.7). None, falls noch nicht vergeben.
    ects : int
        ECTS-Punkte des Moduls.
    abgeschlossen : bool
        Gibt an, ob das Modul abgeschlossen wurde.
    """

    def __init__(self, name: str, ects: int, note: float = None, abgeschlossen: bool = False):
        self.name = name
        self.note = note
        self.ects = ects
        self.abgeschlossen = abgeschlossen

    def set_abgeschlossen(self):
        """
        Markiert das Modul als abgeschlossen.
        """
        self.abgeschlossen = True

    def __str__(self):
        return f"{self.name} (Note: {self.note}, ECTS: {self.ects}, Abgeschlossen: {'Ja' if self.abgeschlossen else 'Nein'})"
