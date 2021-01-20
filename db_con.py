import base64
import os

import env_file
import psycopg2

# from config import config
env_file.load('.env')


def image_to_base64():
    global image_string
    with open("/Users/elenaperez/Desktop/code/fish_images/clownfish.jpg", "rb") as img_file:
        image_string = base64.b64encode(img_file.read())
    return image_string


image_to_base64()


def db_connection():
    try:
        con = psycopg2.connect(
            host=os.getenv('HOST'),
            dbname=os.getenv('DBNAME'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            port=os.getenv('PORT')

        )
        print('You have connected to the db')
        return con
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return False


def insert_data():
    cur = con.cursor()
    cur.execute(
        "INSERT INTO sealife.sealife_data (name, description) VALUES (%s, %s, %s)",
        ('clown fish', 'I live in an anemone', image_string))

    con.commit()
    cur.close()


x = image_to_base64()
con = db_connection()
insert_data()
con.close()

db_connection()
# psycopg2.Binary(image)
