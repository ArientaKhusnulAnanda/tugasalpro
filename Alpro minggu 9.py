import tkinter as tk
from tkinter import ttk, Text, StringVar, END, messagebox
import random
import os

# Fungsi Timer Belajar
def start_timer():
    try:
        minutes = int(timer_entry.get())
        seconds = minutes * 60
        countdown(seconds)
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan angka valid untuk waktu!")

def countdown(seconds):
    if seconds >= 0:
        mins, secs = divmod(seconds, 60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        root.after(1000, countdown, seconds - 1)
    else:
        timer_label.config(text="Waktu Habis!")
        messagebox.showinfo("Notifikasi", "Timer selesai!")

# Fungsi Catatan Harian
# Fungsi untuk menyimpan catatan ke file
# Fungsi untuk menyimpan catatan ke file
def save_note():
    """Fungsi untuk menyimpan catatan ke file."""
    file_path = "catatan_harian.txt"  # Nama file
    try:
        with open(file_path, "w") as file:
            # Menyimpan isi dari widget Text ke dalam file
            file.write(note_text.get("1.0", END).strip())  
        
        # Menghapus teks di widget Text setelah catatan disimpan
        note_text.delete("1.0", END)

        messagebox.showinfo("Notifikasi", f"Catatan disimpan ke {os.path.abspath(file_path)}")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")


# Fungsi untuk membaca catatan dari file dan menampilkannya di aplikasi
def load_notes():
    """Fungsi untuk membaca catatan dari file dan menampilkannya di aplikasi."""
    file_path = "catatan_harian.txt"
    if os.path.exists(file_path):  # Periksa apakah file ada
        try:
            with open(file_path, "r") as file:
                catatan = file.read()  # Membaca isi file
                note_text.delete("1.0", END)  # Menghapus teks yang ada sebelumnya di widget
                note_text.insert("1.0", catatan)  # Menampilkan catatan yang dibaca ke widget Text
            messagebox.showinfo("Notifikasi", "Catatan berhasil dimuat!")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {e}")
    else:
        messagebox.showerror("Error", "Tidak ada catatan yang ditemukan!")


# Fungsi To-Do List
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(END, task)
        task_entry.delete(0, END)

def mark_done():
    selected_task = task_listbox.curselection()
    if selected_task:
        task = task_listbox.get(selected_task)
        task_listbox.delete(selected_task)
        task_listbox.insert(END, f"{task} (Selesai)")

def clear_tasks():
    task_listbox.delete(0, END)

# Fungsi Kalkulator
def add_to_expression(symbol):
    calc_entry_var.set(calc_entry_var.get() + symbol)

def clear_expression():
    calc_entry_var.set("")

def calculate_expression():
    try:
        result = eval(calc_entry_var.get())
        calc_entry_var.set(str(result))
    except Exception:
        messagebox.showerror("Error", "Ekspresi tidak valid!")

# Fungsi Motivational Quote Generator
def show_quote():
    quotes = [
        "Jangan menyerah, keajaiban terjadi setiap hari.",
        "Kesuksesan adalah hasil dari persiapan, kerja keras, dan belajar dari kegagalan.",
        "Hari ini adalah kesempatan untuk lebih baik dari kemarin.",
        "Percayalah pada proses dan dirimu sendiri."
    ]
    random_quote.set(random.choice(quotes))

# Membuat jendela utama
root = tk.Tk()
root.title("Student Productivity Toolkit")
root.geometry("400x600")

# Warna Tema
theme_color = "#F5F5DC"  # Warna beige menarik untuk latar belakang

# Gaya ttk dengan warna frame
style = ttk.Style()
style.configure("TFrame", background=theme_color)
style.configure("TLabel", background=theme_color, font=("Arial", 12))
style.configure("TButton", font=("Arial", 10))

# Menu Navigasi
menu = ttk.Notebook(root)
menu.pack(expand=1, fill="both")

# Frame Timer
frame_timer = ttk.Frame(menu)
menu.add(frame_timer, text="Timer Belajar")

timer_label = ttk.Label(frame_timer, text="00:00", font=("Arial", 24), anchor="center")
timer_label.pack(pady=10)
timer_entry = ttk.Entry(frame_timer, width=10)
timer_entry.pack(pady=5)
start_button = ttk.Button(frame_timer, text="Mulai Timer", command=start_timer)
start_button.pack(pady=5)

# Frame Catatan Harian
frame_notes = ttk.Frame(menu)
menu.add(frame_notes, text="Catatan Harian")

note_text = Text(frame_notes, height=10, width=40, bg="white", fg="black", font=("Arial", 10))
note_text.pack(pady=10)
save_button = ttk.Button(frame_notes, text="Simpan Catatan", command=save_note)
save_button.pack(pady=5)
load_button = ttk.Button(frame_notes, text="Baca Catatan", command=load_notes)
load_button.pack(pady=5)

# Frame To-Do List
frame_todo = ttk.Frame(menu)
menu.add(frame_todo, text="To-Do List")

task_entry = ttk.Entry(frame_todo, width=30)
task_entry.pack(pady=5)
add_task_button = ttk.Button(frame_todo, text="Tambah Tugas", command=add_task)
add_task_button.pack(pady=5)
task_listbox = tk.Listbox(frame_todo, height=10, width=30, bg="white", fg="black")
task_listbox.pack(pady=5)
done_button = ttk.Button(frame_todo, text="Tandai Selesai", command=mark_done)
done_button.pack(pady=5)
clear_button = ttk.Button(frame_todo, text="Hapus Semua", command=clear_tasks)
clear_button.pack(pady=5)

# Frame Kalkulator
frame_calculator = ttk.Frame(menu)
menu.add(frame_calculator, text="Kalkulator")

calc_entry_var = StringVar()
calc_entry = ttk.Entry(frame_calculator, textvariable=calc_entry_var, font=("Arial", 16), justify="right", width=15)
calc_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    action = calculate_expression if text == '=' else clear_expression if text == 'C' else lambda t=text: add_to_expression(t)
    ttk.Button(frame_calculator, text=text, command=action).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Motivational Quote Generator
random_quote = StringVar()
quote_label = ttk.Label(root, textvariable=random_quote, wraplength=300, justify="center")
quote_label.pack(pady=10)
quote_button = ttk.Button(root, text="Tampilkan Motivasi", command=show_quote)
quote_button.pack(pady=5)

root.mainloop()