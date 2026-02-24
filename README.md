# 🔐 Secure Password Generator (Python GUI)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

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

## 🚀 How to Run

1.  **Prerequisites:** Ensure you have Python installed on your system.
2.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/izajugulete-ops/password-generator.git](https://github.com/izajugulete-ops/password-generator.git)
    ```
3.  **Run the Application:**
    ```bash
    python password_generator.py
    ```

## 📂 Project Structure

* `password_generator.py`: The main source code containing the GUI logic and generation algorithms.
* `.gitignore`: Configured to exclude IDE settings and temporary Python files.

## 🚧 Roadmap

- [ ] Add a password strength meter (visual feedback).
- [ ] Implement an option to save passwords to an encrypted local file.
- [ ] Dark mode support for the UI.

---
Developed as part of my personal portfolio to demonstrate GUI development and security-conscious programming in Python.
