# 🏦 Banking System — Object-Oriented Programming in Python

A simple terminal-based banking system built to study and practice Object-Oriented Programming (OOP) in Python. This project was developed as preparation for refactoring a Streamlit application at my internship using OOP principles.

---

## 📚 OOP Concepts Practiced

- **Encapsulation** — account balance and password are protected with `_` and `__` prefixes, preventing direct external access
- **Inheritance** — `ContaCorrente` and `ContaPoupanca` inherit from the base class `ContaBancaria`
- **Polymorphism** — the `sacar()` method behaves differently for each account type
- **Composition** — `Cliente` holds a list of `Conta` objects; `Banco` holds lists of both `Cliente` and `Conta` objects
- **Abstract behavior** — `Transacao` objects are automatically created and stored on every operation

---

## 🗂️ Project Structure

```
├── classes.py   # All classes: ContaBancaria, ContaCorrente, ContaPoupanca, Transacao, Cliente, Banco
└── main.py      # Terminal interface with interactive menu
```

> ⚠️ Variable and method names are written in Portuguese, as this project targets a Brazilian development context.

---

## ⚙️ Features

- Register clients and open checking or savings accounts
- Deposit, withdraw, and transfer between accounts with password validation
- View full transaction history with timestamps
- Monthly interest rendering for savings accounts
- Overdraft limit support for checking accounts

---

## ▶️ How to Run

1. Clone the repository
2. Make sure you have Python 3.10+ installed
3. Run the terminal interface:

```bash
python main.py
```

No external libraries required — only Python's built-in `datetime` module is used.

---

## 💡 Context

This project was built as a study exercise to learn OOP in Python before applying these concepts at my internship, where my team is refactoring a Streamlit app to use an object-oriented architecture.
