# utils/visualizer.py

import matplotlib.pyplot as plt
from db.db_handler import calculate_total_progress, summarize_modules

def zeige_studienfortschritt():
    """
    Zeigt den Gesamtfortschritt des Studiums als horizontales Balkendiagramm.
    """
    fortschritt = calculate_total_progress()

    plt.figure(figsize=(7, 1.2))
    plt.barh([''], [fortschritt], color='lightgreen')
    plt.xlim(0, 100)
    plt.xlabel("Fortschritt in %")
    plt.title("Studienfortschritt")
    plt.text(fortschritt, 0, f"{fortschritt:.2f}%", va='center', ha='left', fontsize=10)
    plt.tight_layout()
    # plt.show()  <--- Entfernen oder auskommentieren

def zeige_durchschnittsnoten_pro_semester():
    """
    Zeigt ein Balkendiagramm mit Durchschnittsnoten je Semester.
    Nur Semester mit mindestens einem benoteten Modul werden angezeigt.
    """
    summary = summarize_modules()
    semester = [f"Sem {row[0]}" for row in summary]
    noten = [round(row[2], 2) for row in summary]

    plt.figure(figsize=(10, 5))
    bars = plt.bar(semester, noten, color='skyblue')
    plt.ylim(1.0, 4.0)  # Notenskala 1.0 (beste) bis 4.0 (schlechteste)
    plt.ylabel("Durchschnittsnote")
    plt.title("Durchschnittsnoten pro Semester")
    plt.gca().invert_yaxis()

    for bar, note in zip(bars, noten):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{note:.2f}",
                 ha='center', va='bottom')

    plt.tight_layout()
    # plt.show()  <--- Entfernen oder auskommentieren
