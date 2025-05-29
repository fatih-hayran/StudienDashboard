# Studienfortschritt Dashboard

Ein lokal ausführbares Python-Dashboard zur Visualisierung und Überwachung des Studienfortschritts.

## Funktionen

- Anzeige des ECTS-Fortschritts als Fortschrittsbalken
- Durchschnittsnotenübersicht
- Filterbare Modulübersicht (mit Noten, Status, Semester)
- Balkendiagramm zur Notenentwicklung über Semester 1–3

## Systemvoraussetzungen

- Python 3.10 oder höher
- Betriebssystem: Windows, macOS oder Linux

## Benötigte Bibliotheken

Bitte installiere die folgenden Pakete im Terminal:

```bash
pip install pandas matplotlib
```

**tkinter** und **sqlite3** sind in der Regel bereits in Python enthalten.  
Falls `tkinter` beim Starten fehlt, bitte je nach Betriebssystem nachinstallieren:


## Projektstruktur

```
StudienDashboard/
├── data/
│   └── studienplan_daten.py
├── db/
│   └── db_handler.py
├── gui/
│   └── main_window.py
├── models/
│   ├── modul.py
│   ├── semester.py
│   ├── student.py
│   └── studiengang.py
├── utils/
│   ├── visualizer.py
│   └── dashboard.db
├── main.py
├── README.md
```

## Installation und Ausführung

### 1. Repository klonen

```bash
git clone https://github.com/fatih-hayran/StudienDashboard.git
cd StudienDashboard
```

Oder ZIP herunterladen und entpacken.

### 2. (Optional) Virtuelle Umgebung erstellen

```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate.bat     # Windows
```

### 3. Abhängigkeiten installieren

```bash
pip install pandas matplotlib
```

### 4. Dashboard starten

```bash
python main.py
```

Alternativ kann auch `gui/main_window.py` direkt ausgeführt werden.

## Kontakt

Fatih Hayran  
IU Internationale Hochschule  
fatih.hayran@iu-study.org
