import tkinter as tk
from tkinter import messagebox
import secrets
import string


def genereaza_parola():
    try:
        lungime = int(entry_lungime.get())
    except ValueError:
        messagebox.showerror("Eroare", "Te rugăm să introduci un număr valid pentru lungime.")
        return


    caractere = ""
    if var_mici.get():
        caractere += string.ascii_lowercase
    if var_mari.get():
        caractere += string.ascii_uppercase
    if var_cifre.get():
        caractere += string.digits
    if var_simboluri.get():
        caractere += string.punctuation


    if not caractere:
        messagebox.showwarning("Atenție", "Trebuie să bifezi cel puțin o opțiune pentru a genera parola!")
        return


    parola = ''.join(secrets.choice(caractere) for i in range(lungime))


    entry_rezultat.config(state='normal')
    entry_rezultat.delete(0, tk.END)
    entry_rezultat.insert(0, parola)
    entry_rezultat.config(state='readonly')


def copiaza_parola():
    parola = entry_rezultat.get()
    if parola:
        root.clipboard_clear()
        root.clipboard_append(parola)
        messagebox.showinfo("Succes", "Parola a fost copiată în clipboard!")
    else:
        messagebox.showwarning("Eroare", "Generează o parolă înainte de a o copia.")


root = tk.Tk()
root.title("Generator Parole")
root.geometry("400x450")
root.resizable(False, False)


tk.Label(root, text="Lungime parolă:", font=("Arial", 10, "bold")).pack(pady=(15, 5))
entry_lungime = tk.Spinbox(root, from_=4, to=128, width=10, justify='center')
entry_lungime.delete(0, "end")
entry_lungime.insert(0, "16")
entry_lungime.pack()


tk.Label(root, text="Configurare complexitate:", font=("Arial", 10, "bold")).pack(pady=(15, 5))

var_mici = tk.BooleanVar(value=True)
var_mari = tk.BooleanVar(value=True)
var_cifre = tk.BooleanVar(value=True)
var_simboluri = tk.BooleanVar(value=False)

frame_optiuni = tk.Frame(root)
frame_optiuni.pack()

tk.Checkbutton(frame_optiuni, text="Litere mici (a-z)", variable=var_mici).pack(anchor="w")
tk.Checkbutton(frame_optiuni, text="Litere mari (A-Z)", variable=var_mari).pack(anchor="w")
tk.Checkbutton(frame_optiuni, text="Cifre (0-9)", variable=var_cifre).pack(anchor="w")
tk.Checkbutton(frame_optiuni, text="Simboluri (@#$%...)", variable=var_simboluri).pack(anchor="w")


btn_genereaza = tk.Button(root, text="GENEREAZĂ PAROLA", command=genereaza_parola,bg="#2196F3", fg="white", font=("Arial", 10, "bold"), width=20)
btn_genereaza.pack(pady=15)


entry_rezultat = tk.Entry(root, font=("Courier", 12), width=30, justify='center', state='readonly')
entry_rezultat.pack(pady=5)

btn_copiaza = tk.Button(root, text="COPIAZĂ PAROLA", command=copiaza_parola,bg="#f4f4f4", font=("Arial", 9))
btn_copiaza.pack(pady=5)

root.mainloop()