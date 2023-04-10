from database import connexion_to_database
class Person:
    def __init__(self, last_name: str, first_name: str, address: str, email: str, birthday: str, description: str, photo_filename: str):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.email = email
        self.birthday = birthday
        self.description = description
        self.photo_filename = photo_filename

    def save_to_database(self):
        connexion = connexion_to_database()
        cursor = connexion.cursor()

        # Insert a new row into the person_data table with the Person object's attributes
        insert_query = f"INSERT INTO person (last_name, first_name, address, email, birthday, description, photo_filename) " \
                       f"VALUES ('{self.last_name}', '{self.first_name}', '{self.address}', '{self.email}', '{self.birthday}', '{self.description}', '{self.photo_filename}');"
        cursor.execute(insert_query)
        connexion.commit()

        cursor.close()
        connexion.close()
        return "Successfully saved"
    
    def get_info_from_database(firstname):
        connexion = connexion_to_database()
        cursor = connexion.cursor()

        # Insert a new row into the person table with the Person object's attributes
        insert_query = f"SELECT last_name, first_name, address, email, birthday, description, photo_filename FROM person WHERE first_name='{firstname}'"
        cursor.execute(insert_query)
        result = cursor.fetchone()
        print(result)
        cursor.close()
        connexion.close()
        return result
