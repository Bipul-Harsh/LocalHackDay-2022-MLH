import sqlite3

def insert_note(title, description):
    '''
    Insert a note in the database
    '''
    cursor.execute(f"INSERT INTO notes(title, description) VALUES ('{title}', '{description}')")

def update_note(id, title, description):
    '''
    Update a note in the database
    '''
    cursor.execute(f"UPDATE notes SET title='{title}', description='{description}' WHERE id={id}")

def show_notes():
    '''
    Show all notes in the database

    Returns:
        A list of tuples containing the notes
    '''
    cursor.execute("SELECT * FROM notes")
    return cursor.fetchall()

def print_notes():
    '''
    Print all notes in the database
    '''
    notes = show_notes()
    if len(notes) == 0:
        print("No notes found")
    else:
        for note in show_notes():
            print(f"ID: {note[0]}\nTitle: {note[1]}\nDescription: {note[2]}\n\n")

def delete_note(id):
    '''
    Delete a note from the database
    '''
    cursor.execute(f"DELETE FROM notes WHERE id={id}")

if __name__ == "__main__":
    sqliteConnection = sqlite3.connect('notes.db')
    cursor = sqliteConnection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS notes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(30),
        description VARCHAR(100),
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )""")

    print("Select an option: ")
    print("1. Insert a note")
    print("2. Update a note")
    print("3. Show all notes")
    print("4. Delete a note")
    
    try:
        opt = int(input("Option: "))
    except ValueError:
        print("Invalid option")
        exit()
    
    if opt == 1:
        title = input("Title: ")
        description = input("Description: ")
        insert_note(title, description)
        print("Note inserted")
    elif opt == 2:
        id = input("ID: ")
        title = input("Title: ")
        description = input("Description: ")
        update_note(id, title, description)
        print("Note updated")
    elif opt == 3:
        print_notes()
    elif opt == 4:
        id = input("ID: ")
        delete_note(id)
        print("Note deleted")
    else:
        print("Invalid option")
    
    sqliteConnection.commit()
    sqliteConnection.close()