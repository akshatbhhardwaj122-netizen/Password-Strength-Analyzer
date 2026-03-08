# 🔐 Password Strength Analyzer

A simple **Cybersecurity GUI tool built with Python and Tkinter** that
analyzes the strength of a password in real-time. This tool helps users
create **secure passwords** by checking important security criteria such
as length, character diversity, numbers, and special characters.

------------------------------------------------------------------------

## 📌 Features

-   Real-time password strength detection
-   Strength levels:
    -   Weak
    -   Fair
    -   Good
    -   Strong
-   Progress bar visualization of password strength
-   Checks for:
    -   Minimum password length
    -   Uppercase and lowercase letters
    -   Numbers
    -   Special characters
-   Simple and user-friendly GUI

------------------------------------------------------------------------

## 🖥️ Demo

When a user types a password, the application analyzes it instantly and
displays the strength using a **progress meter and color indicator**.

Example:

  Password     Strength
  ------------ ----------
  12345        Weak
  hello123     Fair
  Hello123     Good
  Hello@1234   Strong

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   Python
-   Tkinter (GUI Framework)
-   Regex (re module)
-   ttk for progress bar

------------------------------------------------------------------------

## 📂 Project Structure

    Password-Strength-Analyzer
    │
    ├── password_strength_analyzer.py
    └── README.md

------------------------------------------------------------------------

## ⚙️ Installation

1.  Clone the repository

```{=html}
<!-- -->
```
    git clone https://github.com/your-username/password-strength-analyzer.git

2.  Navigate to the project folder

```{=html}
<!-- -->
```
    cd password-strength-analyzer

3.  Run the program

```{=html}
<!-- -->
```
    python password_strength_analyzer.py

------------------------------------------------------------------------

## 📊 How It Works

The password strength is calculated using four main rules:

-   Password length (≥ 8 characters)
-   Combination of uppercase and lowercase letters
-   Presence of numbers
-   Presence of special characters

Each rule increases the strength score, and the final score determines
whether the password is **Weak, Fair, Good, or Strong**.

------------------------------------------------------------------------

## 🎯 Purpose

Weak passwords are one of the most common causes of **security breaches
and brute‑force attacks**. This project demonstrates basic
**cybersecurity principles** for evaluating password security.

------------------------------------------------------------------------

## 🚀 Future Improvements

-   Password breach detection using HaveIBeenPwned API
-   Password crack-time estimation
-   Password suggestion generator
-   Web version using Flask
-   Dark mode interface

------------------------------------------------------------------------

## 👨‍💻 Author

Your Name

If you like this project, consider giving it a ⭐ on GitHub!
