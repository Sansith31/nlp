import mariadb

# Connecting to the database
def connect():
    global cursor
    try:
        connect = mariadb.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "sdms"
        )
        cursor = connect.cursor()
    except:
        print("Failed to retreive database!")

def store(id, name, dob, gender, contact, email, pathway):
    cursor.execute(
        f"""INSERT INTO student
        VALUES ({id}, "{name}", {dob}, "{gender}", {contact}, "{email}", "{pathway}");"""
    )