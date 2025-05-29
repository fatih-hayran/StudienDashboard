# main.py

import sqlite3
from tabulate import tabulate

from models.student import Student
from models.studiengang import Studiengang
from data.studienplan_daten import erstelle_studienplan
from db.db_handler import (
    initialize_database,
    insert_modul,
    fetch_all_modules,
    calculate_total_progress,
    summarize_modules
)
from gui.main_window import starte_gui


def reset_modul_datenbank():
    """
    Entfernt bestehende Modul-Daten aus der Datenbank
    und setzt den ID-Zähler zurück.
    """
    connection = sqlite3.connect("dashboard.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Modul;")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='Modul';")
    connection.commit()
    connection.close()


# 1. Datenbankstruktur sicherstellen
initialize_database()

# 2. Bestehende Modul-Daten zurücksetzen (optional)
reset_modul_datenbank()

# 3. Studiengang und Student initialisieren
studiengang = Studiengang("Applied Artificial Intelligence", regelstudienzeit=6)
student = Student(name="Max Mustermann", matrikelnummer="123456", studiengang=studiengang)

# 4. Studienplan laden und Module in Datenbank schreiben
semester_liste = erstelle_studienplan()
for sem in semester_liste:
    studiengang.add_semester(sem)
    for modul in sem.module:
        insert_modul(modul.name, modul.note, modul.ects, modul.abgeschlossen, sem.semester_nr)

# 5. Ausgabe: Basisinformationen
print(f"Name: {student.name}")
print(f"Matrikelnummer: {student.matrikelnummer}")
print(f"Studienfortschritt: {student.get_studienfortschritt():.2f}%")
print(f"Notendurchschnitt: {student.get_notendurchschnitt():.2f}")
print(f"Regelstudienzeit eingehalten: {studiengang.ist_regelstudienzeit_eingehalten()}")

# 6. Ausgabe: Semesterzusammenfassung
print("\nZusammenfassung der Semester:")
headers = ["Semester", "Module", "Durchschnittsnote"]
print(tabulate(summarize_modules(), headers=headers, tablefmt="fancy_grid"))

# 7. Ausgabe: Alle Module
print("\nAlle Module in der Datenbank:")
headers = ["ID", "Name", "Note", "Abgeschlossen", "Semester-ID"]
print(tabulate(fetch_all_modules(), headers=headers, tablefmt="grid"))

# 8. GUI starten
starte_gui()
