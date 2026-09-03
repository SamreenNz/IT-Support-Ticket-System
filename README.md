# IT Support Ticket Management System

A Python and MySQL based backend application for managing IT support tickets efficiently.

## 📌 Project Overview

The **IT Support Ticket Management System** is designed to help an IT support team manage user issues from ticket creation to resolution and closure.

The application provides a simple command-line interface (CLI) and uses MySQL to store and manage ticket information.

## 🚀 Features

* Create support tickets
* View all tickets
* Search tickets by Ticket ID
* Assign tickets to support engineers
* Update ticket status
* Resolve tickets with resolution details
* Close resolved tickets
* Filter tickets by status or priority
* View ticket statistics
* Input validation and error handling

## 🛠️ Technologies Used

* **Python**
* **MySQL**
* **mysql-connector-python**
* **XAMPP / phpMyAdmin**

## 📂 Project Structure

```text
IT_Support_Ticket_System/
├── database.py
├── ticket_functions.py
├── main.py
├── README.md
├── .gitignore
├── requirements.txt
└── database.sql
```

## 🗄️ Database

The project uses a MySQL database named:

```text
it_support
```

The main table is:

```text
tickets
```

The database structure is available in `database.sql`.

## ⚙️ Setup Instructions

### 1. Start MySQL

Start **MySQL** from XAMPP Control Panel.

### 2. Create the Database

Open phpMyAdmin and execute the SQL commands from:

```text
database.sql
```

### 3. Install Python Dependency

Open Command Prompt in the project folder and run:

```bash
pip install -r requirements.txt
```

### 4. Check Database Configuration

Open:

```text
database.py
```

Make sure the MySQL connection details match your local MySQL setup.

### 5. Run the Application

Run:

```bash
python main.py
```

## 🎯 Ticket Workflow

```text
Create Ticket
      ↓
Assign Ticket
      ↓
Update Status
      ↓
Resolve Ticket
      ↓
Close Ticket
```

## 🔮 Future Enhancements

Possible future improvements include:

* Web-based frontend
* User authentication
* Role-based access control
* Admin dashboard
* Email notifications
* Ticket priority automation
* Reports and analytics

## 👩‍💻 Author

**Samreen Naaz**

MCA | Python | MySQL | IT Support | Software Development
