# phonebook_app.py
import psycopg2
import csv

#connection to db
conn = psycopg2.connect(
    host = 'localhost',
    dbname = 'phonebook',
    user = 'postgres',
    password = 'admin123',
    port = 5432
)
cur = conn.cursor()

#create table if it doesnt exist
cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL
)
""")
conn.commit()


def import_from_csv(filename):
    try:
        with open(filename, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    cur.execute(
                        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                        (row['name'], row['phone'])
                    )
                except psycopg2.IntegrityError:
                    conn.rollback()  # skip duplicates
                    print(f"Skipping duplicate: {row}")
                else:
                    conn.commit()
        print("CSV import completed!")
    except FileNotFoundError:
        print("File not found!")

#by hand add contacts
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    try:
        cur.execute(
            "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
            (name, phone)
        )
        conn.commit()
        print("Contact added!")
    except psycopg2.IntegrityError:
        conn.rollback()
        print("Phone already exists! Contact not added.")


def update_contact():
    choice = input("Update by (1) name or (2) phone: ")

    if choice == "1":
        old_name = input("Enter current name: ")
        new_name = input("Enter new name: ")
        cur.execute(
            "UPDATE phonebook SET name=%s WHERE name=%s",
            (new_name, old_name)
        )

    elif choice == "2":
        old_phone = input("Enter current phone: ")
        new_phone = input("Enter new phone: ")
        try:
            cur.execute(
                "UPDATE phonebook SET phone=%s WHERE phone=%s",
                (new_phone, old_phone)
            )
            conn.commit()
        except psycopg2.IntegrityError:
            conn.rollback()
            print("Phone number already exists! Update failed.")
            return

    conn.commit()
    print("Updated successfully!")


def query_contacts():
    print("1. Show all")
    print("2. Search by name")
    print("3. Search by phone")

    choice = input("Choose: ")

    if choice == "1":
        cur.execute("SELECT * FROM phonebook")

    elif choice == "2":
        name = input("Enter name: ")
        cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", ('%' + name + '%',))

    elif choice == "3":
        phone = input("Enter phone: ")
        cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", ('%' + phone + '%',))

    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
    else:
        print("No contacts found.")


def delete_contact():
    choice = input("Delete by (1) name or (2) phone: ")

    if choice == "1":
        name = input("Enter name: ")
        cur.execute("DELETE FROM phonebook WHERE name=%s", (name,))

    elif choice == "2":
        phone = input("Enter phone: ")
        cur.execute("DELETE FROM phonebook WHERE phone=%s", (phone,))

    conn.commit()
    print("Deleted successfully!")


def menu():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Add contact")
        print("2. Import from CSV")
        print("3. Update contact")
        print("4. Query contacts")
        print("5. Delete contact")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            filename = input("Enter CSV filename: ")
            import_from_csv(filename)
        elif choice == "3":
            update_contact()
        elif choice == "4":
            query_contacts()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice! Try again.")

#main loop
menu()

#sever connection
cur.close()
conn.close()
