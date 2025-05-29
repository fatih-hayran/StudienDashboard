# db/db_handler.py

import sqlite3

DB_NAME = "dashboard.db"

def initialize_database():
    """
    Erstellt die SQLite-Datenbank und alle benötigten Tabellen,
    falls sie noch nicht existieren.
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    # Tabellen erstellen
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Studiengang (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            regelstudienzeit INTEGER
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            matrikelnummer TEXT,
            studiengang_id INTEGER,
            FOREIGN KEY (studiengang_id) REFERENCES Studiengang (id)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Semester (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            semester_nr INTEGER,
            studiengang_id INTEGER,
            FOREIGN KEY (studiengang_id) REFERENCES Studiengang (id)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Modul (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            note REAL,
            ects INTEGER,
            abgeschlossen BOOLEAN,
            semester_id INTEGER,
            FOREIGN KEY (semester_id) REFERENCES Semester (id)
        );
    """)

    connection.commit()
    connection.close()
    print("Tabellen erfolgreich erstellt!")

def insert_modul(name: str, note: float, ects: int, abgeschlossen: bool, semester_id: int):
    """
    Fügt ein Modul in die Datenbank ein.
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO Modul (name, note, ects, abgeschlossen, semester_id)
        VALUES (?, ?, ?, ?, ?);
    """, (name, note, ects, abgeschlossen, semester_id))

    connection.commit()
    connection.close()
    print(f"Modul '{name}' erfolgreich hinzugefügt!")

def fetch_all_modules():
    """
    Gibt alle Module aus der Datenbank zurück.
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, note, abgeschlossen, semester_id FROM Modul;
    """)
    rows = cursor.fetchall()

    connection.close()
    return rows

def calculate_progress(semester_id: int) -> float:
    """
    Berechnet den Fortschritt (in %) für ein einzelnes Semester.
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*) FROM Modul WHERE semester_id = ?;
    """, (semester_id,))
    total = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*) FROM Modul WHERE semester_id = ? AND abgeschlossen = 1;
    """, (semester_id,))
    done = cursor.fetchone()[0]

    connection.close()

    return round((done / total) * 100, 2) if total > 0 else 0.0

def calculate_total_progress() -> float:
    """
    Berechnet den gesamten Studienfortschritt.
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM Modul;")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM Modul WHERE abgeschlossen = 1;")
    completed = cursor.fetchone()[0]

    connection.close()

    print(f"Debug: DB - Completed Modules = {completed}, Total Modules = {total}")
    return round((completed / total) * 100, 2) if total > 0 else 0.0

def summarize_modules():
    """
    Gibt für jedes Semester die Anzahl der Module und den Notenschnitt zurück.
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT semester_id, COUNT(*), AVG(note)
        FROM Modul
        WHERE note IS NOT NULL
        GROUP BY semester_id;
    """)
    summary = cursor.fetchall()

    connection.close()
    return summary

def calculate_ects_progress():
    """
    Gibt zurück: (abgeschlossene ECTS, gesamte ECTS)
    """
    import sqlite3
    connection = sqlite3.connect("dashboard.db")
    cursor = connection.cursor()

    cursor.execute("SELECT SUM(ects) FROM Modul;")
    total = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(ects) FROM Modul WHERE abgeschlossen = 1;")
    done = cursor.fetchone()[0] or 0

    connection.close()
    return done, total

def calculate_average_grade():
    """
    Gibt den gewichteten Notendurchschnitt aller abgeschlossenen Module zurück.
    """
    connection = sqlite3.connect("dashboard.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT note, ects FROM Modul
        WHERE note IS NOT NULL AND abgeschlossen = 1;
    """)
    rows = cursor.fetchall()
    connection.close()

    total_weighted = 0
    total_ects = 0
    for note, ects in rows:
        total_weighted += note * ects
        total_ects += ects

    if total_ects == 0:
        return 0.0
    return round(total_weighted / total_ects, 2)
