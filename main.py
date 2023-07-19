import sqlite3
import os

connection = sqlite3.connect("Contacts.db")

cursor = connection.cursor()

database_file = 'Contacts.db'

def storeinfo (name, phone, email):
    print("working...")
    insert_data_query = 'INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)'
    cursor.execute(insert_data_query, (name, phone, email))
    connection.commit()
     

class Operations:
    def see_contacts(self):
        cursor.execute("SELECT * FROM contacts")
        result = cursor.fetchall()
        print(result)
        Begin.main_menu(self)

    def add_contacts(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        storeinfo(name, phone, email)
        Begin.main_menu(self)
    
    def delete_contacts(self):
        name = input("Enter name: ")
        sql = "DELETE FROM contacts WHERE name = ?"
        cursor.execute(sql, (name,))
        connection.commit()
        print("Contact deleted")
        Begin.main_menu(self)

    def update_contacts(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        sql = "UPDATE contacts SET phone = ?, email = ? WHERE name = ?"
        cursor.execute(sql, (phone, email, name))
        connection.commit()
        print("Contact updated")
        Begin.main_menu(self)

class Begin(Operations):
    def check_if_database_exists(self, database_file):
        print("databases does not exist")
        print("creating databases...")
        print("Preapring charts...")
        create_table_query = '''CREATE TABLE IF NOT EXISTS contacts (
                    name TEXT,
                    phone TEXT,
                    email TEXT)'''
        cursor.execute(create_table_query)
        create_table_query2 = "CREATE TABLE IF NOT EXISTS users (name TEXT, password TEXT)"
        cursor.execute(create_table_query2)
        connection.commit()
        print("databases created")
    
    def user_check(self):
        choice = int(input("1. Login\n2. Register\n"))
        if choice == 1:
            name = input("Enter name: ")
            password = input("Enter password: ")
            sql = "SELECT * FROM users WHERE name = ? AND password = ?"
            values = (name, password)
            cursor.execute(sql, values)
            result = cursor.fetchall()

            if result:
                print("Login successful")
                self.main_menu()
            else:
                print("Login failed")
                self.user_check()

        else:
            new_name = input("Enter new name: ")
            new_password = input("Enter new password: ")
            sql = "INSERT INTO users ('name', 'password') VALUES (?,?)"
            values = (new_name, new_password)
            cursor.execute(sql, values)
            connection.commit()
            print("Registration successful")

    def main_menu(self):
        print("1. see contacts\n2. add contacts\n3. delete contacts\n4. update contacts\n5. exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            Operations.see_contacts(self)
        elif choice == 2:
            Operations.add_contacts(self)
        elif choice == 3:
            Operations.delete_contacts(self)
        elif choice == 4:
            Operations.update_contacts(self)
        elif choice == 5:
            exit()


    

def main():
    mystart = Begin()
    mystart.check_if_database_exists(database_file)
    mystart.user_check()
    mystart.main_menu()

main()