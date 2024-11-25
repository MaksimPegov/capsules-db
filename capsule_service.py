from init_db import get_db_connection

def create_capsule(name: str, value: str, password: str = None):
    conn = get_db_connection()
    cur = conn.cursor()

    if password:
        cur.execute("INSERT INTO capsules (name, value, password) VALUES (%s, %s, %s)", (name, value, password))
    else:
        cur.execute("INSERT INTO capsules (name, value) VALUES (%s, %s)", (name, value))

    conn.commit()

    cur.close()
    conn.close()

    return 201

def get_capsule(name: str, password: str = None):
    conn = get_db_connection()
    cur = conn.cursor()

    if password is not None:
        cur.execute("SELECT value FROM capsules WHERE name = %s AND password = %s", (name, password))
    else:
        cur.execute("SELECT value FROM capsules WHERE name = %s", (name,))

    result = cur.fetchone()

    cur.close()
    conn.close()

    return result

