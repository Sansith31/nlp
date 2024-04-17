import mariadb

# Connecting to the database
def connect():
    global cursor
    global conn
    try:
        conn = mariadb.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "sdms"
        )
        cursor = conn.cursor()
    except:
        print("Failed to retreive database!")

def store(id, name, dob, gender, contact, email, pathway):
    cursor.execute(
        f"""INSERT INTO student
        VALUES ({id}, "{name}", "{dob}", "{gender}", {contact}, "{email}", "{pathway}");"""
    )

def commit():
    global conn
    conn.commit()
    conn.close()