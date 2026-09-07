from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)


def get_database_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="it_support"
    )
@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/dashboard")
def dashboard():

    connection = get_database_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM tickets")
    total_tickets = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tickets WHERE status = 'Open'")
    open_tickets = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tickets WHERE status = 'In Progress'")
    in_progress = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tickets WHERE status = 'Resolved'")
    resolved = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tickets WHERE status = 'Closed'")
    closed = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return render_template(
        "dashboard.html",
        total_tickets=total_tickets,
        open_tickets=open_tickets,
        in_progress=in_progress,
        resolved=resolved,
        closed=closed
    )


@app.route("/create-ticket", methods=["GET", "POST"])
def create_ticket_page():

    if request.method == "POST":

        user_name = request.form["user_name"]
        issue = request.form["issue"]
        description = request.form["description"]
        priority = request.form["priority"]

        connection = get_database_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO tickets
            (user_name, issue, description, priority)
            VALUES (%s, %s, %s, %s)
            """,
            (user_name, issue, description, priority)
        )

        connection.commit()

        cursor.close()
        connection.close()

        return redirect(url_for("home"))

    return render_template("create_ticket.html")


@app.route("/tickets")
def view_tickets_page():

    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
    SELECT ticket_id, user_name, issue, description,
           priority, status, assigned_to, resolution, created_at
    FROM tickets
    ORDER BY ticket_id DESC
""")
    tickets = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("tickets.html", tickets=tickets)


@app.route("/search-ticket", methods=["GET", "POST"])
def search_ticket_page():

    if request.method == "POST":

        ticket_id = request.form["ticket_id"]

        connection = get_database_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT ticket_id, user_name, issue, description,
                   priority, status, assigned_to, resolution, created_at
            FROM tickets
            WHERE ticket_id = %s
            """,
            (ticket_id,)
        )

        ticket = cursor.fetchone()

        cursor.close()
        connection.close()

        return render_template(
            "search_ticket.html",
            ticket=ticket
        )

    return render_template(
        "search_ticket.html",
        ticket=None
    )
@app.route("/update-status", methods=["GET", "POST"])
def update_status_page():

    message = None
    ticket = None

    if request.method == "POST":

        ticket_id = request.form["ticket_id"]
        new_status = request.form["status"]

        connection = get_database_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT *
            FROM tickets
            WHERE ticket_id = %s
            """,
            (ticket_id,)
        )

        ticket = cursor.fetchone()

        if ticket:

            cursor.execute(
                """
                UPDATE tickets
                SET status = %s
                WHERE ticket_id = %s
                """,
                (new_status, ticket_id)
            )

            connection.commit()

            ticket["status"] = new_status
            message = "Ticket status updated successfully."

        else:
            message = "Ticket not found."

        cursor.close()
        connection.close()

    return render_template(
        "update_status.html",
        ticket=ticket,
        message=message
    )
@app.route("/assign-ticket", methods=["GET", "POST"])
def assign_ticket_page():

    message = None
    ticket = None

    if request.method == "POST":

        ticket_id = request.form["ticket_id"]
        assigned_to = request.form["assigned_to"]

        connection = get_database_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT *
            FROM tickets
            WHERE ticket_id = %s
            """,
            (ticket_id,)
        )

        ticket = cursor.fetchone()

        if ticket:

            cursor.execute(
                """
                UPDATE tickets
                SET assigned_to = %s
                WHERE ticket_id = %s
                """,
                (assigned_to, ticket_id)
            )

            connection.commit()

            ticket["assigned_to"] = assigned_to
            message = "Ticket assigned successfully."

        else:
            message = "Ticket not found."

        cursor.close()
        connection.close()

    return render_template(
        "assign_ticket.html",
        ticket=ticket,
        message=message
    )
@app.route("/resolve-ticket", methods=["GET", "POST"])
def resolve_ticket_page():

    message = None
    ticket = None

    if request.method == "POST":

        ticket_id = request.form["ticket_id"]
        resolution = request.form["resolution"]

        connection = get_database_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT *
            FROM tickets
            WHERE ticket_id = %s
            """,
            (ticket_id,)
        )

        ticket = cursor.fetchone()

        if ticket:

            cursor.execute(
                """
                UPDATE tickets
                SET resolution = %s,
                    status = 'Resolved'
                WHERE ticket_id = %s
                """,
                (resolution, ticket_id)
            )

            connection.commit()

            ticket["resolution"] = resolution
            ticket["status"] = "Resolved"

            message = "Ticket resolved successfully."

        else:
            message = "Ticket not found."

        cursor.close()
        connection.close()

    return render_template(
        "resolve_ticket.html",
        ticket=ticket,
        message=message
    )
@app.route("/close-ticket", methods=["GET", "POST"])
def close_ticket_page():

    message = None
    ticket = None

    if request.method == "POST":

        ticket_id = request.form["ticket_id"]

        connection = get_database_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT *
            FROM tickets
            WHERE ticket_id = %s
            """,
            (ticket_id,)
        )

        ticket = cursor.fetchone()

        if ticket:

            if ticket["status"] == "Resolved":

                cursor.execute(
                    """
                    UPDATE tickets
                    SET status = 'Closed'
                    WHERE ticket_id = %s
                    """,
                    (ticket_id,)
                )

                connection.commit()

                ticket["status"] = "Closed"
                message = "Ticket closed successfully."

            else:
                message = "Ticket cannot be closed. It must be Resolved first."

        else:
            message = "Ticket not found."

        cursor.close()
        connection.close()

    return render_template(
        "close_ticket.html",
        ticket=ticket,
        message=message
    )
    
@app.route("/filter-tickets", methods=["GET", "POST"])
def filter_tickets_page():

    tickets = []

    status = request.form.get("status", "")
    priority = request.form.get("priority", "")

    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT ticket_id, user_name, issue, priority,
               status, assigned_to, created_at
        FROM tickets
        WHERE 1=1
    """

    parameters = []

    if status:
        query += " AND status = %s"
        parameters.append(status)

    if priority:
        query += " AND priority = %s"
        parameters.append(priority)

    query += " ORDER BY ticket_id DESC"

    cursor.execute(query, parameters)

    tickets = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "filter_tickets.html",
        tickets=tickets,
        selected_status=status,
        selected_priority=priority
    )


@app.route("/statistics")
def statistics_page():
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
    SELECT
        COUNT(*) AS total,
        SUM(CASE WHEN status = 'Open' THEN 1 ELSE 0 END) AS open_tickets,
        SUM(CASE WHEN status = 'In Progress' THEN 1 ELSE 0 END) AS in_progress,
        SUM(CASE WHEN status = 'Resolved' THEN 1 ELSE 0 END) AS resolved,
        SUM(CASE WHEN status = 'Closed' THEN 1 ELSE 0 END) AS closed,
        SUM(CASE WHEN priority = 'Low' THEN 1 ELSE 0 END) AS low_count,
        SUM(CASE WHEN priority = 'Medium' THEN 1 ELSE 0 END) AS medium_count,
        SUM(CASE WHEN priority = 'High' THEN 1 ELSE 0 END) AS high_count
    FROM tickets
""")

    statistics = cursor.fetchone()

    cursor.close()
    connection.close()

    return render_template(
        "statistics.html",
        statistics=statistics
    )



if __name__ == "__main__":
    app.run(debug=True)