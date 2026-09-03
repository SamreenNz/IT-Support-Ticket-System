from ticket_functions import (
    create_ticket,
    view_tickets,
    search_ticket,
    update_ticket_status,
    assign_ticket,
    resolve_ticket,
    close_ticket,
    filter_tickets,
    ticket_statistics
)


def main():

    while True:

        print("\n===================================")
        print("     IT SUPPORT TICKET SYSTEM")
        print("===================================")
        print("1. Create Ticket")
        print("2. View All Tickets")
        print("3. Search Ticket")
        print("4. Update Ticket Status")
        print("5. Assign Ticket")
        print("6. Resolve Ticket")
        print("7. Close Ticket")
        print("8. Filter Tickets")
        print("9. Ticket Statistics")
        print("10. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            create_ticket()

        elif choice == "2":
            view_tickets()

        elif choice == "3":
            search_ticket()

        elif choice == "4":
            update_ticket_status()

        elif choice == "5":
            assign_ticket()

        elif choice == "6":
            resolve_ticket()

        elif choice == "7":
            close_ticket()

        elif choice == "8":
            filter_tickets()

        elif choice == "9":
            ticket_statistics()

        elif choice == "10":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please try again.")


main()