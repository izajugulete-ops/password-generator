# 🔐 Secure Password Generator (Python GUI)

A desktop application designed to generate cryptographically strong passwords with a customizable user interface. This tool allows users to define length and complexity requirements to ensure high-standard digital security.

## ✨ Features

* **Cryptographically Secure:** Uses the Python `secrets` module for generating random characters, making passwords suitable for sensitive accounts.
* **Customizable Complexity:** Users can toggle between lowercase letters, uppercase letters, digits, and special symbols.
* **Adjustable Length:** Supports password lengths from 4 to 128 characters using an intuitive spinbox control.
* **One-Click Copy:** Integrated clipboard functionality allows users to quickly copy generated passwords.
* **Input Validation:** Robust error handling to prevent invalid lengths or empty character set selections.

## 🛠️ Tech Stack

* **Language:** Python
* **GUI Framework:** Tkinter (standard Python interface to the Tcl/Tk GUI toolkit)
* **Security:** `secrets` module (designed for managing secrets such as passwords and security tokens)
