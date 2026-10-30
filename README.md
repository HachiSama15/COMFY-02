# STUDENT REGISTRATION SYSTEM
### FINAL PROJECT 101

> **PRINT, IF/ELSE, TAS LOOPS LANG TO!**
>
> *Yung mga may hashtag (#) are notes/explanations.*

---

## MY INFORMATION

### Paano Nagwo-work?

- **One Big While Loop** – Mas basic ito kaysa lagyan pa natin ng `def` (function). The entire system runs inside one main `while` loop.
- **Screen Variable** – The variable `screen` determines which screen to display:
  - `main` – Main menu
  - `dashboard` – Student/Admin dashboard
  - `edit` – Edit personal information
- **CSV Storage** – All data are saved in three CSV files:
  - `StudsF.csv`
  - `StudentsAcc.csv`
  - `Admin.csv`

  **NOTE:** Hindi agad makikita ang mga CSV files kapag dinownload or ni-run ninyo ang code for the first time. Automatically silang magagawa once the program runs and data are registered or saved. Okeh?

- **Default Student Password** – The initial password of each student is their own Student Number (e.g., `26-050030`).

- **Simplified CSV Handling** – Each CSV file is read once at the start of the program. Whenever there are changes, the entire list of records is saved again, starting with the header row followed by all the data rows.

---

## LIBRARIES USED

### 1. `csv`
Used for reading and writing CSV files. Dito naka-store yung mga student records, accounts, and admin information.

### 2. `os`
Parang nakikipag-communicate siya with the operating system. It checks whether the required files exist and clears the terminal screen when needed.

### 3. `re`
Stands for **Regular Expressions**. Used to validate user inputs based on predefined patterns, such as:
- Student Numbers
- Email Addresses
- Phone Numbers

### 4. `getpass`
Used instead of the regular `input()` function when entering passwords. This hides the password while the user types, providing an additional layer of privacy.

---

## ======= READ ME =======

Please check the other file included in this repository. You can download and read it to better understand how the system works and how its different functions operate.

### DISCLAIMER

AI po 'yan! HAHAHA. Bale, sinend ko yung buong code ko sa AI and asked it to explain the different functions. Need niyo na lang silang i-familiarize, and feel free to ask AI for help kung may parts na hindi ninyo maintindihan.

Pero please, aralin pa rin natin yung buong system. Don't just rely on the explanations. We should understand how the actual code works, especially since this is our final project.

Yon lang! Salamat.

---

**////jiyan2k26**
