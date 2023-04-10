import mysql.connector
def connexion_to_database():
    connexion = mysql.connector.connect(user='Manohy', password='', host='localhost', database='sahy_project')
    return connexion