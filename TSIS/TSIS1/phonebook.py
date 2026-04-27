# phonebook_app.py
import psycopg2
import json
import csv

# ----------------------------
# 1. Connection
# ----------------------------
conn = psycopg2.connect(
    host='localhost',
    dbname='phonebook',
    user='postgres',
    password='admin123',
    port=5432
)
cur = conn.cursor()

# ----------------------------
# 2. Schema
# ----------------------------
cur.execute("""
-- DROP old function (important)
DROP FUNCTION IF EXISTS search_contacts(TEXT);

-- TABLES
CREATE TABLE IF NOT EXISTS groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    email TEXT,
    birthday DATE,
    group_id INT REFERENCES groups(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS phones (
    id SERIAL PRIMARY KEY,
    contact_id INT REFERENCES contacts(id) ON DELETE CASCADE,
    phone VARCHAR(20),
    type VARCHAR(10) CHECK (type IN ('home','work','mobile'))
);

-- default groups
INSERT INTO groups(name)
VALUES ('Family'), ('Work'), ('Friend'), ('Other')
ON CONFLICT DO NOTHING;

-- FUNCTIONS
CREATE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE(id INT, name TEXT, email TEXT, phone TEXT, group_name TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        c.id,
        c.name::TEXT,
        c.email::TEXT,
        ph.phone::TEXT,
        g.name::TEXT
    FROM contacts c
    LEFT JOIN phones ph ON ph.contact_id = c.id
    LEFT JOIN groups g ON g.id = c.group_id
    WHERE c.name ILIKE '%' || p_query || '%'
       OR c.email ILIKE '%' || p_query || '%'
       OR ph.phone ILIKE '%' || p_query || '%';
END;
$$ LANGUAGE plpgsql;

-- PROCEDURES
CREATE OR REPLACE PROCEDURE add_phone(p_contact_name TEXT, p_phone TEXT, p_type TEXT)
LANGUAGE plpgsql
AS $$
DECLARE cid INT;
BEGIN
    SELECT id INTO cid FROM contacts WHERE name=p_contact_name;
    IF cid IS NULL THEN
        RAISE EXCEPTION 'Contact not found';
    END IF;

    INSERT INTO phones(contact_id, phone, type)
    VALUES (cid, p_phone, p_type);
END;
$$;

CREATE OR REPLACE PROCEDURE move_to_group(p_contact_name TEXT, p_group TEXT)
LANGUAGE plpgsql
AS $$
DECLARE gid INT;
BEGIN
    INSERT INTO groups(name) VALUES (p_group)
    ON CONFLICT (name) DO NOTHING;

    SELECT id INTO gid FROM groups WHERE name=p_group;

    UPDATE contacts SET group_id=gid WHERE name=p_contact_name;
END;
$$;
""")

conn.commit()

# ----------------------------
# 3. Add Contact
# ----------------------------
def add_contact():
    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday (YYYY-MM-DD): ")
    group = input("Group: ")
    phone = input("Phone: ")
    ptype = input("Type (home/work/mobile): ")

    try:
        cur.execute("""
            INSERT INTO contacts(name,email,birthday)
            VALUES (%s,%s,%s)
            ON CONFLICT (name) DO NOTHING
        """, (name,email,birthday))

        cur.execute("CALL move_to_group(%s,%s)", (name,group))
        cur.execute("CALL add_phone(%s,%s,%s)", (name,phone,ptype))

        conn.commit()
        print("Added!")
    except Exception as e:
        conn.rollback()
        print(e)

# ----------------------------
# 4. Search
# ----------------------------
def search():
    q = input("Search: ")
    cur.execute("SELECT * FROM search_contacts(%s)", (q,))
    for row in cur.fetchall():
        print(row)

# ----------------------------
# 5. Filter by group
# ----------------------------
def filter_group():
    g = input("Group: ")
    cur.execute("""
        SELECT c.name, c.email
        FROM contacts c
        JOIN groups g ON c.group_id=g.id
        WHERE g.name=%s
    """,(g,))
    print(cur.fetchall())

# ----------------------------
# 6. Sort
# ----------------------------
def sort_contacts():
    print("1.Name 2.Birthday 3.Date added")
    choice = input()

    col = {"1":"name","2":"birthday","3":"created_at"}.get(choice,"name")

    cur.execute(f"SELECT name,email,birthday FROM contacts ORDER BY {col}")
    print(cur.fetchall())

# ----------------------------
# 7. Pagination
# ----------------------------
def paginate():
    limit=3
    offset=0

    while True:
        cur.execute("""
            SELECT name,email FROM contacts
            ORDER BY id
            LIMIT %s OFFSET %s
        """,(limit,offset))

        for r in cur.fetchall():
            print(r)

        cmd=input("n/p/q: ")
        if cmd=="n": offset+=limit
        elif cmd=="p": offset=max(0,offset-limit)
        else: break

# ----------------------------
# 8. Export JSON
# ----------------------------
def export_json():
    cur.execute("""
        SELECT c.name,c.email,c.birthday,g.name,ph.phone,ph.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id=g.id
        LEFT JOIN phones ph ON ph.contact_id=c.id
    """)
    data=cur.fetchall()

    with open("export.json","w") as f:
        json.dump(data,f,indent=4,default=str)

    print("Exported!")

# ----------------------------
# 9. Import JSON
# ----------------------------
def import_json():
    with open("export.json") as f:
        data=json.load(f)

    for row in data:
        name=row[0]

        cur.execute("SELECT id FROM contacts WHERE name=%s",(name,))
        if cur.fetchone():
            choice=input(f"{name} exists skip/overwrite: ")
            if choice=="skip": continue
            cur.execute("DELETE FROM contacts WHERE name=%s",(name,))

        cur.execute("""
            INSERT INTO contacts(name,email,birthday)
            VALUES (%s,%s,%s)
        """,(row[0],row[1],row[2]))

        cur.execute("CALL move_to_group(%s,%s)",(row[0],row[3]))
        cur.execute("CALL add_phone(%s,%s,%s)",(row[0],row[4],row[5]))

    conn.commit()
    print("Imported!")

# ----------------------------
# 10. CSV Import
# ----------------------------
def import_csv():
    file=input("CSV file: ")

    with open(file) as f:
        reader=csv.DictReader(f)
        for r in reader:
            name=r["name"]

            cur.execute("""
                INSERT INTO contacts(name,email,birthday)
                VALUES (%s,%s,%s)
                ON CONFLICT DO NOTHING
            """,(r["name"],r["email"],r["birthday"]))

            cur.execute("CALL move_to_group(%s,%s)",(name,r["group"]))
            cur.execute("CALL add_phone(%s,%s,%s)",(name,r["phone"],r["type"]))

    conn.commit()
    print("CSV imported!")

# ----------------------------
# 11. Menu
# ----------------------------
def menu():
    while True:
        print("\n1.Add\n2.Search\n3.Filter group\n4.Sort\n5.Paginate\n6.Export\n7.Import JSON\n8.Import CSV\n9.Exit")
        c=input()

        if c=="1": add_contact()
        elif c=="2": search()
        elif c=="3": filter_group()
        elif c=="4": sort_contacts()
        elif c=="5": paginate()
        elif c=="6": export_json()
        elif c=="7": import_json()
        elif c=="8": import_csv()
        elif c=="9": break

menu()

cur.close()
conn.close()
