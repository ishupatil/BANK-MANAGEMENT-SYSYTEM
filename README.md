# 🏦 Bank Management System (Python Console App)

This is a simple **Bank Management System** built in Python using file-based storage with `JSON`. It simulates core banking operations like account creation, deposits, withdrawals, account updates, and deletion — all managed through a terminal interface.

---

## 🚀 Features

- ✅ Create a new bank account (auto-generates account number)
- 💰 Deposit money (max ₹10,000 at a time)
- 💸 Withdraw money (with balance validation)
- 👤 View account details (PIN-protected)
- ✏️ Update account information (except age, account number, balance)
- ❌ Delete bank account with confirmation
- 🔒 PIN authentication for all sensitive operations
- 📦 Data is persisted in `data.json`

---

## 📁 Data Format (`data.json`)

```json
[
  {
    "name": "Isha",
    "email": "isha203@gamil.com",
    "pin": 2003,
    "age": 23,
    "accountNo": "@3k89EJ",
    "balance": 0
  },
  {
    "name": "Shubham",
    "age": 21,
    "email": "shubham21@gmail.com",
    "pin": "3124",
    "accountNo": "8%W7tw4",
    "balance": 500
  }
]
🛠️ Tech Stack
Python 3.x

Standard Libraries:

json – for storing user data

random and string – for generating account numbers

pathlib – for checking file existence

🧑‍💻 How to Run
Make sure Python 3 is installed.

Save the code as main.py.

Create a data.json file in the same directory (you can use an empty list []).

Run the script:
python main.py
Choose an option from the menu:

Press 1 for creating your account
Press 2 for depositing money in bank
Press 3 for withdrawing money from bank
Press 4 for details
Press 5 for updating details
Press 6 for deleting your account
![image](https://github.com/user-attachments/assets/09343b9c-846c-44e3-94ac-2e16e19128a5)

✅ Validations & Constraints
PIN must be 4 digits

Users must be at least 18 years old to open an account

Deposits must not exceed ₹10,000 at a time

Withdrawals are only allowed if sufficient balance is available

All sensitive actions require account number and PIN

🔐 Security Notes
PIN input is currently not hidden (consider using getpass module for masking in future versions)

No encryption is used — this app is designed for learning purposes only

📈 Future Improvements
GUI using Tkinter or PyQt

Password masking using getpass

Transaction history tracking

Login/logout system

Error logging

🧑‍🎓 Author
Made by [Ishwaree Patil]
For educational purposes — beginner-friendly project to understand file handling and basic OOP in Python.

📝 License
This project is open-source and free to use. Attribution appreciated.


---

Let me know if you'd like:
- A GUI version of this system
- How to turn this into a **Tkinter desktop app**
- GitHub `repository setup` + `.gitignore`

I'd be happy to help!











