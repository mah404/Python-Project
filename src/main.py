import csv
import os
from datetime import datetime
import socket


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")


def load_users():
    # This function reads the users.csv file and returns all users as a list.
    users_file = os.path.join(DATA_DIR, "users.csv")

    # If the file does not exist, show an error and return an empty list.
    if not os.path.exists(users_file):
        print("ERROR: users.csv was not found.")
        return []

    try:
        with open(users_file, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            users = list(reader)

        return users

    except Exception as error:
        print(f"ERROR reading users.csv: {error}")
        return []


def get_missing_user_fields(users):
    # This function checks missing required fields in the user list.
    required_fields = ["username", "name", "department", "email", "active"]
    missing_entries = []

    for user in users:
        username = user.get("username", "unknown")

        for field in required_fields:
            if user.get(field, "").strip() == "":
                missing_entries.append(
                    f"Missing field: {field} for user {username}"
                )

    return missing_entries


def validate_users():
    # This function checks if users have missing required fields or are inactive.
    users = load_users()

    if not users:
        return

    missing_entries = get_missing_user_fields(users)

    print("\nUser validation result:")
    print("=======================")

    if missing_entries:
        for entry in missing_entries:
            print(entry)
    else:
        print("No missing required fields found.")

    for user in users:
        if user.get("active", "").lower() == "no":
            print(f"Inactive user: {user.get('username')} - {user.get('name')}")


def load_tickets():
    # This function reads tickets.csv and returns all tickets as a list.
    tickets_file = os.path.join(DATA_DIR, "tickets.csv")

    if not os.path.exists(tickets_file):
        print("ERROR: tickets.csv was not found.")
        return []

    try:
        with open(tickets_file, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            tickets = list(reader)

        return tickets

    except Exception as error:
        print(f"ERROR reading tickets.csv: {error}")
        return []


def show_ticket_overview():
    # This function shows all tickets from the CSV file.
    tickets = load_tickets()

    if not tickets:
        return

    print("\nTicket overview:")
    print("================")

    for ticket in tickets:
        print(
            f"{ticket.get('ticket_id', '')} | "
            f"{ticket.get('requester', '')} | "
            f"{ticket.get('category', '')} | "
            f"{ticket.get('priority', '')} | "
            f"{ticket.get('status', '')} | "
            f"{ticket.get('short_description', '')}"
        )


def summarize_tickets():
    # This function counts tickets by status, priority and category.
    tickets = load_tickets()

    if not tickets:
        return

    status_count = {}
    priority_count = {}
    category_count = {}

    for ticket in tickets:
        status = ticket.get("status", "unknown")
        priority = ticket.get("priority", "unknown")
        category = ticket.get("category", "unknown")

        status_count[status] = status_count.get(status, 0) + 1
        priority_count[priority] = priority_count.get(priority, 0) + 1
        category_count[category] = category_count.get(category, 0) + 1

    print("\nTickets by status:")
    print(status_count)

    print("\nTickets by priority:")
    print(priority_count)

    print("\nTickets by category:")
    print(category_count)


def show_critical_tickets():
    # This function shows open tickets with high priority.
    tickets = load_tickets()

    if not tickets:
        return

    print("\nCritical open tickets:")
    print("======================")

    found = False

    for ticket in tickets:
        if ticket.get("priority") == "hoch" and ticket.get("status") == "offen":
            found = True
            print(
                f"{ticket.get('ticket_id', '')} | "
                f"{ticket.get('requester', '')} | "
                f"{ticket.get('short_description', '')}"
            )

    if not found:
        print("No critical open tickets found.")


def analyze_log():
    # This function counts INFO, WARNING and ERROR lines in support.log.
    log_file = os.path.join(DATA_DIR, "support.log")

    if not os.path.exists(log_file):
        print("ERROR: support.log was not found.")
        return {"INFO": 0, "WARNING": 0, "ERROR": 0}

    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    try:
        with open(log_file, "r", encoding="utf-8") as file:
            for line in file:
                if "INFO" in line:
                    counts["INFO"] += 1
                elif "WARNING" in line:
                    counts["WARNING"] += 1
                elif "ERROR" in line:
                    counts["ERROR"] += 1

    except Exception as error:
        print(f"ERROR reading support.log: {error}")
        return {"INFO": 0, "WARNING": 0, "ERROR": 0}

    print("\nLog analysis:")
    print("=============")
    print(f"INFO: {counts['INFO']}")
    print(f"WARNING: {counts['WARNING']}")
    print(f"ERROR: {counts['ERROR']}")

    return counts


def show_system_snapshot():
    # This function reads the snapshot file from the reports folder.
    snapshot_file = os.path.join(REPORTS_DIR, "system_snapshot.txt")

    if not os.path.exists(snapshot_file):
        print("ERROR: system_snapshot.txt was not found.")
        print("Please run ./scripts/collect_snapshot.sh first.")
        return

    try:
        with open(snapshot_file, "r", encoding="utf-8") as file:
            print(file.read())

    except Exception as error:
        print(f"ERROR reading system_snapshot.txt: {error}")


def create_report():
    # This function creates a support report in the reports folder.
    users = load_users()
    tickets = load_tickets()

    if not users:
        print("Report was not created because users.csv is missing or empty.")
        return

    if not tickets:
        print("Report was not created because tickets.csv is missing or empty.")
        return

    log_counts = analyze_log()

    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)

    report_file = os.path.join(REPORTS_DIR, "support_report.txt")

    open_tickets = [t for t in tickets if t.get("status") == "offen"]
    high_priority_tickets = [t for t in tickets if t.get("priority") == "hoch"]
    critical_tickets = [
        t for t in tickets
        if t.get("priority") == "hoch" and t.get("status") == "offen"
    ]

    missing_entries = get_missing_user_fields(users)

    try:
        with open(report_file, "w", encoding="utf-8") as file:
            file.write("Nordstern Helpdesk Support Report\n")
            file.write("=================================\n")
            file.write(f"Created at: {datetime.now()}\n")
            file.write(f"Hostname: {socket.gethostname()}\n\n")

            file.write(f"Number of users: {len(users)}\n")

            file.write("Missing required user fields:\n")
            if missing_entries:
                for entry in missing_entries:
                    file.write(f"- {entry}\n")
            else:
                file.write("- No missing required fields found.\n")

            file.write(f"\nTotal tickets: {len(tickets)}\n")
            file.write(f"Open tickets: {len(open_tickets)}\n")
            file.write(f"High priority tickets: {len(high_priority_tickets)}\n\n")

            file.write("Critical open tickets:\n")
            if critical_tickets:
                for ticket in critical_tickets:
                    file.write(
                        f"- {ticket.get('ticket_id')}: "
                        f"{ticket.get('short_description')}\n"
                    )
            else:
                file.write("- No critical open tickets found.\n")

            file.write("\nLog entries:\n")
            file.write(f"ERROR: {log_counts['ERROR']}\n")
            file.write(f"WARNING: {log_counts['WARNING']}\n")

            file.write("\nTechnical evaluation:\n")
            file.write(
                "The tool found open high-priority tickets and log entries. "
                "These points should be checked by the IT support team.\n"
            )

        print(f"Support report created: {report_file}")

    except Exception as error:
        print(f"ERROR creating support report: {error}")


def main_menu():
    # This function shows the menu and handles user input.
    while True:
        print("\nNordstern Helpdesk Tool")
        print("=======================")
        print("1. Show system snapshot")
        print("2. Check user list")
        print("3. Show ticket overview")
        print("4. Analyze tickets by priority and status")
        print("5. Show critical open tickets")
        print("6. Analyze log file")
        print("7. Create support report")
        print("8. Exit program")

        choice = input("Choose an option: ")

        if choice == "1":
            show_system_snapshot()
        elif choice == "2":
            validate_users()
        elif choice == "3":
            show_ticket_overview()
        elif choice == "4":
            summarize_tickets()
        elif choice == "5":
            show_critical_tickets()
        elif choice == "6":
            analyze_log()
        elif choice == "7":
            create_report()
        elif choice == "8":
            print("Program ended.")
            break
        else:
            print("Invalid input. Please choose a number from 1 to 8.")


main_menu()