import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from db.db_handler import (
    calculate_total_progress,
    calculate_ects_progress,
    summarize_modules,
    fetch_all_modules
)

def starte_gui():
    root = tk.Tk()
    root.title("Studienfortschritt Dashboard")
    root.geometry("1500x950")
    root.configure(bg="white")

    # === SECTION 1 ===
    section1 = tk.Frame(root, bg="white", pady=20)
    section1.pack(fill="x")

    center_kpis = tk.Frame(section1, bg="white")
    center_kpis.pack(anchor="center")

    fortschritt = calculate_total_progress()
    ects_done, ects_total = calculate_ects_progress()
    summary = summarize_modules()
    durchschnitt = sum(row[2] for row in summary) / len(summary) if summary else 0.0

    # Box 1: Studienfortschritt + ECTS
    box1 = tk.Frame(center_kpis, bg="white", width=480, height=150, relief="solid", bd=1)
    box1.pack_propagate(False)
    box1.pack(side="left", padx=40)

    tk.Label(box1, text="Studienfortschritt", font=("Helvetica", 18, "bold"), bg="white").pack(pady=(10, 0))
    pb = ttk.Progressbar(box1, length=280, mode="determinate")
    pb["value"] = fortschritt
    pb.pack()
    tk.Label(box1, text=f"{fortschritt:.2f}%", font=("Helvetica", 14), bg="white").pack()
    tk.Label(box1, text=f"{ects_done} von {ects_total} ECTS erreicht", font=("Helvetica", 12), bg="white").pack(pady=(0, 5))

    # Box 2: Notendurchschnitt
    box2 = tk.Frame(center_kpis, bg="white", width=480, height=150, relief="solid", bd=1)
    box2.pack_propagate(False)
    box2.pack(side="left", padx=40)

    tk.Label(box2, text="\u00d8 Note", font=("Helvetica", 18, "bold"), bg="white").pack(pady=(10, 0))
    tk.Label(box2, text=f"{durchschnitt:.2f}", font=("Helvetica", 34, "bold"), bg="white").pack()

    # === SECTION 2 ===
    tk.Frame(root, height=2, bg="#c0c0c0").pack(fill="x", pady=10)
    section2 = tk.Frame(root, bg="white")
    section2.pack(pady=(10, 30))

    # Box: Modulübersicht mit Filter (zentriert, gesamte Breite)
    table_box = tk.Frame(section2, bg="white", width=1000, height=400, relief="solid", bd=1)
    table_box.pack_propagate(False)
    table_box.pack(anchor="center")

    tk.Label(table_box, text="Modul\u00fcbersicht", font=("Helvetica", 14, "bold"), bg="white").pack(pady=(5, 2))

    filter_frame = tk.Frame(table_box, bg="white")
    filter_frame.pack()

    tk.Label(filter_frame, text="Semester:", font=("Helvetica", 12), bg="white").pack(side="left")
    semester_options = ["Alle"] + [str(row[0]) for row in summary]
    semester_var = tk.StringVar(value="Alle")
    semester_dropdown = ttk.Combobox(filter_frame, textvariable=semester_var, values=semester_options, width=8, font=("Helvetica", 11))
    semester_dropdown.pack(side="left", padx=5)

    columns = ("ID", "Name", "Note", "Abgeschlossen", "Semester")
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))
    style.configure("Treeview", font=("Helvetica", 11))

    tree = ttk.Treeview(table_box, columns=columns, show="headings", height=14)
    for col in columns:
        tree.heading(col, text=col)
        stretch_width = 360 if col == "Name" else 140
        tree.column(col, anchor="center", width=stretch_width)

    def update_table(*args):
        selected = semester_var.get()
        tree.delete(*tree.get_children())
        for modul in fetch_all_modules():
            abgeschlossen = "Ja" if modul[3] else "Nein"
            note = modul[2] if modul[2] is not None else "-"
            if selected == "Alle" or str(modul[4]) == selected:
                tree.insert("", "end", values=(modul[0], modul[1], note, abgeschlossen, modul[4]))

    semester_dropdown.bind("<<ComboboxSelected>>", update_table)
    update_table()
    tree.pack(pady=5)

    # === SECTION 3 ===
    tk.Frame(root, height=2, bg="#c0c0c0").pack(fill="x", pady=10)
    section3 = tk.Frame(root, bg="white")
    section3.pack(pady=(10, 30))

    diagramm_box = tk.Frame(section3, bg="white", width=480, height=170, relief="solid", bd=1)
    diagramm_box.pack_propagate(False)
    diagramm_box.pack(anchor="w", padx=40)

    tk.Label(diagramm_box, text="Notenentwicklung (Semester 1–3)", font=("Helvetica", 18, "bold"), bg="white").pack(
        pady=(10, 0))

    semester_labels = ["Sem 1", "Sem 2", "Sem 3", "Sem 4", "Sem 5", "Sem 6"]
    noten = [row[2] for row in summary if row[0] in [1, 2, 3]]

    fig, ax = plt.subplots(figsize=(4.0, 1.6))
    bars = ax.bar(semester_labels[:3], noten, color="skyblue", width=0.3)
    ax.set_ylim(0.0, 4.0)
    ax.set_ylabel("Ø Note", fontsize=6)
    ax.set_title("Ø Noten in den ersten 3 Semestern", fontsize=8)
    for bar, note in zip(bars, noten):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.03, f"{note:.2f}",
                ha='center', va='bottom', fontsize=6)

    diagram_canvas = FigureCanvasTkAgg(fig, master=diagramm_box)
    diagram_canvas.draw()
    diagram_canvas.get_tk_widget().pack(expand=True)

    # === Start der GUI ===
    root.mainloop()
