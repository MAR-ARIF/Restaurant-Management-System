Restaurant Management System (Python CLI Application)

A fully interactive command-line Restaurant Management System built in Python. It provides a complete ordering flow for customers and a secure admin panel for managing menu items, coupon codes, pricing, and tax settings.

🚀 Features
👨‍🍳 Customer Interface

Browse menu categories (Starters, Mains, Sides, Drinks, Desserts)

Select items using numeric codes

Automatic price calculation

Coupon code validation & discounts

Optional service charge

Tax calculation

Detailed order summary and receipt

Payment confirmation

🔐 Admin Panel

Secure login using SHA-256 hashed passwords

Set and change admin password

Add new menu items

Update prices of existing items

Modify tax rate

Add, view, and delete coupon codes

View full restaurant menu

🗂 Data Persistence

Menu stored in menu.json

Coupon codes in coupon_code.json

Admin password stored securely in admin.txt

Maintains data across sessions

🛠️ Technologies Used

Python 3

json for data storage

hashlib for password hashing

getpass for secure inputs

datetime for timestamps

📂 How to Run
python Restaurent\ management\ system.py


Make sure menu.json, coupon_code.json, and admin.txt exist or will be automatically created on first run.

📌 Future Improvements

GUI version (Tkinter or PyQt)

Database integration (MySQL)

User accounts for repeat customers

Receipt saving as PDF

📄 Author

Developed by Md. Afrajur Rahman Arif as a Python project for practicing data handling, secure login flows, and menu-driven application design.
