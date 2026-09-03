# IT Support Ticket Management System

## Project Description

The IT Support Ticket Management System is a Python and MySQL based application designed to manage IT support tickets efficiently.

The system allows users to create, view, search, assign, update, resolve, close, and filter support tickets. It also provides ticket statistics based on status and priority.

## Features

- Create new support tickets
- View all tickets
- Search tickets by Ticket ID
- Update ticket status
- Assign tickets to support engineers
- Resolve tickets with resolution details
- Close resolved tickets
- Filter tickets by status or priority
- View ticket statistics
- Input validation and error handling

## Technologies Used

- Python
- MySQL
- mysql-connector-python

## Database

The project uses a MySQL database named `it_support`.

The main table used by the application is:

`tickets`

## Project Structure

```text
IT-Support-Ticket-System/
├── database.py
├── ticket_functions.py
├── main.py
├── README.md
└── .gitignore