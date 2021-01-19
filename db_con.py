import psycopg2
import os
import env_file
env_file.load('.env')

#image = open('/Users/elenaperez/Desktop/code/fish_images/clownfish.jpg', 'rb').read()

def db_connection():
    try:
        con = psycopg2.connect(
            host = os.getenv('HOST'),
            dbname = os.getenv('DBNAME'),
            user = os.getenv('USER'),
            password = os.getenv('PASSWORD'),
            port = os.getenv('PORT')
        )
        print('You have connected to the db')
        return con
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return False


def insert_data():
    cur = con.cursor()
    cur.execute("INSERT INTO sealife.sealife_data (name, description) VALUES ('clown fish', 'I live in an anemone')")

    con.commit()
    cur.close()    


con = db_connection()
insert_data()
con.close()

db_connection()
#psycopg2.Binary(image)