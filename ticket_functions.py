from database import connection


def create_ticket():
    print("\n===== CREATE NEW TICKET =====")

    # Validate user name
    while True:
        user_name = input("Enter your name: ").strip()

        if user_name:
            break
        else:
            print("Name cannot be empty. Please try again.")

    # Validate issue title
    while True:
        issue = input("Enter issue title: ").strip()

        if issue:
            break
        else:
            print("Issue title cannot be empty. Please try again.")

    # Validate description
    while True:
        description = input("Enter issue description: ").strip()

        if description:
            break
        else:
            print("Issue description cannot be empty. Please try again.")

    # Select priority
    while True:
        print("\nSelect Priority:")
        print("1. Low")
        print("2. Medium")
        print("3. High")

        priority_choice = input("Enter choice: ").strip()

        if priority_choice == "1":
            priority = "Low"
            break
        elif priority_choice == "2":
            priority = "Medium"
            break
        elif priority_choice == "3":
            priority = "High"
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    query = """
        INSERT INTO tickets
        (user_name, issue, description, priority)
        VALUES (%s, %s, %s, %s)
    """

    values = (user_name, issue, description, priority)

    try:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()

        print("\nTicket created successfully!")
        print("Ticket ID:", cursor.lastrowid)

    except Exception as error:
        print("\nUnable to create ticket.")
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()

def view_tickets():
    print("\n===== ALL TICKETS =====")

    query = "SELECT * FROM tickets"

    try:
        cursor = connection.cursor()
        cursor.execute(query)

        tickets = cursor.fetchall()

        if len(tickets) == 0:
            print("No tickets found.")
        else:
            for ticket in tickets:
                print("\nTicket ID:", ticket[0])
                print("User:", ticket[1])
                print("Issue:", ticket[2])
                print("Description:", ticket[3])
                print("Priority:", ticket[4])
                print("Status:", ticket[5])
                print("Assigned To:", ticket[6])
                print("Resolution:", ticket[7])
                print("Created At:", ticket[8])

    except Exception as error:
        print("\nUnable to retrieve tickets.")
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()


def search_ticket():
    print("\n===== SEARCH TICKET =====")

    # Validate Ticket ID
    while True:
        ticket_id = input("Enter Ticket ID: ").strip()

        if ticket_id.isdigit() and int(ticket_id) > 0:
            break

        print("Invalid Ticket ID. Please enter a positive number.")

    query = "SELECT * FROM tickets WHERE ticket_id = %s"

    try:
        cursor = connection.cursor()
        cursor.execute(query, (ticket_id,))

        ticket = cursor.fetchone()

        if ticket:
            print("\nTicket Found!")
            print("----------------------------")
            print("Ticket ID:", ticket[0])
            print("User:", ticket[1])
            print("Issue:", ticket[2])
            print("Description:", ticket[3])
            print("Priority:", ticket[4])
            print("Status:", ticket[5])
            print("Assigned To:", ticket[6])
            print("Resolution:", ticket[7])
            print("Created At:", ticket[8])
        else:
            print("\nNo ticket found with this ID.")

    except Exception as error:
        print("\nUnable to search ticket.")
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()


def update_ticket_status():
    print("\n===== UPDATE TICKET STATUS =====")

    # Validate Ticket ID
    while True:
        ticket_id = input("Enter Ticket ID: ").strip()

        if ticket_id.isdigit() and int(ticket_id) > 0:
            break

        print("Invalid Ticket ID. Please enter a positive number.")

    # Select status
    while True:
        print("\nSelect New Status:")
        print("1. Open")
        print("2. In Progress")
        print("3. Resolved")

        status_choice = input("Enter choice: ").strip()

        if status_choice == "1":
            status = "Open"
            break
        elif status_choice == "2":
            status = "In Progress"
            break
        elif status_choice == "3":
            status = "Resolved"
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    query = """
        UPDATE tickets
        SET status = %s
        WHERE ticket_id = %s
    """

    try:
        cursor = connection.cursor()
        cursor.execute(query, (status, ticket_id))
        connection.commit()

        if cursor.rowcount > 0:
            print("\nTicket status updated successfully!")
            print("Ticket ID:", ticket_id)
            print("New Status:", status)
        else:
            print("\nTicket not found.")

    except Exception as error:
        print("\nUnable to update ticket status.")
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()

            
def assign_ticket():
    print("\n===== ASSIGN TICKET =====")

    # Validate Ticket ID
    while True:
        ticket_id = input("Enter Ticket ID: ").strip()

        if ticket_id.isdigit() and int(ticket_id) > 0:
            break

        print("Invalid Ticket ID. Please enter a positive number.")

    # Validate Support Engineer Name
    while True:
        assigned_to = input("Enter Support Engineer Name: ").strip()

        if assigned_to:
            break

        print("Support Engineer Name cannot be empty. Please try again.")

    query = """
        UPDATE tickets
        SET assigned_to = %s
        WHERE ticket_id = %s
    """

    try:
        cursor = connection.cursor()
        cursor.execute(query, (assigned_to, ticket_id))
        connection.commit()

        if cursor.rowcount > 0:
            print("\nTicket assigned successfully!")
            print("Ticket ID:", ticket_id)
            print("Assigned To:", assigned_to)
        else:
            print("\nTicket not found.")

    except Exception as error:
        print("\nUnable to assign ticket.")
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()

def resolve_ticket():
    print("\n===== RESOLVE TICKET =====")

    # Validate Ticket ID
    while True:
        ticket_id = input("Enter Ticket ID: ").strip()

        if ticket_id.isdigit() and int(ticket_id) > 0:
            break

        print("Invalid Ticket ID. Please enter a positive number.")

    # Validate Resolution
    while True:
        resolution = input("Enter Resolution: ").strip()

        if resolution:
            break

        print("Resolution cannot be empty. Please try again.")

    query = """
        UPDATE tickets
        SET resolution = %s,
            status = 'Resolved'
        WHERE ticket_id = %s
    """

    try:
        cursor = connection.cursor()
        cursor.execute(query, (resolution, ticket_id))
        connection.commit()

        if cursor.rowcount > 0:
            print("\nTicket resolved successfully!")
            print("Ticket ID:", ticket_id)
            print("Status: Resolved")
            print("Resolution:", resolution)
        else:
            print("\nTicket not found.")

    except Exception as error:
        print("\nUnable to resolve ticket.")
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()
def close_ticket():
    print("\n===== CLOSE TICKET =====")

    # Validate Ticket ID
    while True:
        ticket_id = input("Enter Ticket ID: ").strip()

        if ticket_id.isdigit() and int(ticket_id) > 0:
            break

        print("Invalid Ticket ID. Please enter a positive number.")

    try:
        cursor = connection.cursor()

        query = "SELECT status FROM tickets WHERE ticket_id = %s"
        cursor.execute(query, (ticket_id,))

        ticket = cursor.fetchone()

        if ticket is None:
            print("\nTicket not found.")
            return

        current_status = ticket[0]

        if current_status == "Closed":
            print("\nTicket is already closed.")
            return

        if current_status != "Resolved":
            print("\nTicket cannot be closed.")
            print("Current Status:", current_status)
            print("Please resolve the ticket first.")
            return

        update_query = """
            UPDATE tickets
            SET status = 'Closed'
            WHERE ticket_id = %s
        """

        cursor.execute(update_query, (ticket_id,))
        connection.commit()

        print("\nTicket closed successfully!")
        print("Ticket ID:", ticket_id)
        print("Status: Closed")

    except Exception as error:
        print("\nUnable to close ticket.")
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()


def filter_tickets():
    print("\n===== FILTER TICKETS =====")

    print("1. Filter by Status")
    print("2. Filter by Priority")

    choice = input("Enter choice: ").strip()

    if choice == "1":

        print("\n===== SELECT STATUS =====")
        print("1. Open")
        print("2. In Progress")
        print("3. Resolved")
        print("4. Closed")

        status_choice = input("Enter choice: ").strip()

        if status_choice == "1":
            status = "Open"
        elif status_choice == "2":
            status = "In Progress"
        elif status_choice == "3":
            status = "Resolved"
        elif status_choice == "4":
            status = "Closed"
        else:
            print("Invalid status choice.")
            return

        query = "SELECT * FROM tickets WHERE status = %s"
        value = (status,)

    elif choice == "2":

        print("\n===== SELECT PRIORITY =====")
        print("1. Low")
        print("2. Medium")
        print("3. High")

        priority_choice = input("Enter choice: ").strip()

        if priority_choice == "1":
            priority = "Low"
        elif priority_choice == "2":
            priority = "Medium"
        elif priority_choice == "3":
            priority = "High"
        else:
            print("Invalid priority choice.")
            return

        query = "SELECT * FROM tickets WHERE priority = %s"
        value = (priority,)

    else:
        print("Invalid choice.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute(query, value)

        tickets = cursor.fetchall()

        if len(tickets) == 0:
            print("\nNo tickets found.")
        else:
            print("\n===== FILTERED TICKETS =====")

            for ticket in tickets:
                print("\nTicket ID:", ticket[0])
                print("User:", ticket[1])
                print("Issue:", ticket[2])
                print("Priority:", ticket[4])
                print("Status:", ticket[5])
                print("Assigned To:", ticket[6])

    except Exception as error:
        print("\nUnable to filter tickets.")
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()

def ticket_statistics():
    print("\n===== TICKET STATISTICS =====")

    try:
        cursor = connection.cursor()

        # Total tickets
        cursor.execute("SELECT COUNT(*) FROM tickets")
        total_tickets = cursor.fetchone()[0]

        # Tickets by status
        cursor.execute("""
            SELECT status, COUNT(*)
            FROM tickets
            GROUP BY status
        """)
        status_data = cursor.fetchall()

        # Tickets by priority
        cursor.execute("""
            SELECT priority, COUNT(*)
            FROM tickets
            GROUP BY priority
        """)
        priority_data = cursor.fetchall()

        print("\nTotal Tickets:", total_tickets)

        print("\n--- Tickets by Status ---")

        statuses = {
            "Open": 0,
            "In Progress": 0,
            "Resolved": 0,
            "Closed": 0
        }

        for status, count in status_data:
            statuses[status] = count

        print("Open:", statuses["Open"])
        print("In Progress:", statuses["In Progress"])
        print("Resolved:", statuses["Resolved"])
        print("Closed:", statuses["Closed"])

        print("\n--- Tickets by Priority ---")

        priorities = {
            "Low": 0,
            "Medium": 0,
            "High": 0
        }

        for priority, count in priority_data:
            priorities[priority] = count

        print("Low:", priorities["Low"])
        print("Medium:", priorities["Medium"])
        print("High:", priorities["High"])

    except Exception as error:
        print("\nUnable to retrieve ticket statistics.")
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()