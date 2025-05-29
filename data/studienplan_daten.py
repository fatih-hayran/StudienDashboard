# data/studienplan_daten.py

from models.modul import Modul
from models.semester import Semester

def erstelle_studienplan():
    """
    Gibt eine Liste aller Semester mit zugehörigen Modulen zurück.
    Semester 1–3 sind abgeschlossen mit Noten, Semester 4–6 offen.
    """
    semester_liste = []

    # Semester 1 (abgeschlossen)
    sem1 = Semester(semester_nr=1)
    sem1.module = [
        Modul("Artificial Intelligence", 5, 1.3, True),
        Modul("Einführung in das wissenschaftliche Arbeiten", 5, 1.7, True),
        Modul("Einführung in die Programmierung mit Python", 5, 1.7, True),
        Modul("Mathematik: Analysis", 5, 1.3, True),
        Modul("IT-Management", 5, 1.7, True),
        Modul("Englisch für die Berufswelt", 5, 1.7, True),
    ]
    semester_liste.append(sem1)

    # Semester 2 (abgeschlossen)
    sem2 = Semester(semester_nr=2)
    sem2.module = [
        Modul("Kollaboratives Arbeiten", 5, 2.0, True),
        Modul("Statistik – Wahrscheinlichkeit und deskriptive Statistik", 5, 1.7, True),
        Modul("Objektorientierte und funktionale Programmierung mit Python", 5, 1.7, True),
        Modul("Mathematik: Lineare Algebra", 5, 2.0, True),
        Modul("Selbstmanagement", 5, 1.7, True),
        Modul("Technologische Trends und Digitalisierung", 5, 1.3, True),
    ]
    semester_liste.append(sem2)

    # Semester 3 (abgeschlossen)
    sem3 = Semester(semester_nr=3)
    sem3.module = [
        Modul("Interkulturelle und ethische Handlungskompetenz", 5, 1.7, True),
        Modul("Statistik – Schließende Statistik", 5, 1.7, True),
        Modul("Cloud Computing", 5, 1.7, True),
        Modul("Cloud Programming", 5, 1.3, True),
        Modul("Projektmanagement", 5, 1.7, True),
        Modul("Agile Softwareentwicklung", 5, 1.7, True),
    ]
    semester_liste.append(sem3)

    # Semester 4 (offen)
    sem4 = Semester(semester_nr=4)
    sem4.module = [
        Modul("Maschinelles Lernen – Supervised Learning", 5),
        Modul("Maschinelles Lernen – Unsupervised Learning und Feature Engineering", 5),
        Modul("Neuronale Netze und Deep Learning", 5),
        Modul("Einführung in Computer Vision", 5),
        Modul("Data Warehouse und Data Lakes", 5),
        Modul("Big Data Technologien", 5),
    ]
    semester_liste.append(sem4)

    # Semester 5 (offen)
    sem5 = Semester(semester_nr=5)
    sem5.module = [
        Modul("Projekt: Computer Vision", 5),
        Modul("Einführung in das Reinforcement Learning", 5),
        Modul("Einführung in NLP", 5),
        Modul("Projekt: NLP", 5),
        Modul("Einführung in Datenschutz und IT-Sicherheit", 5),
        Modul("Data Science Software Engineering", 5),
        Modul("Projekt: Vom Modell zum Produktvertrieb", 5),
        Modul("Seminar: Ethische Fragen der Data Science", 5),
    ]
    semester_liste.append(sem5)

    # Semester 6 (offen)
    sem6 = Semester(semester_nr=6)
    sem6.module = [
        Modul("User Experience", 5),
        Modul("UX-Projekt oder Projekt: Edge AI", 5),
        Modul("Bachelorarbeit", 10),
    ]
    semester_liste.append(sem6)

    return semester_liste
