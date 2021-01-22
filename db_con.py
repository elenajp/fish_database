import base64
import os

import env_file
import psycopg2

env_file.load('.env')

directory = '/Users/elenaperez/Desktop/code/fish_images/'
image_list = []


def images_to_list():
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            image_list.append(filename)


images_to_list()

print(image_list)


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
    with open("/Users/elenaperez/Desktop/code/fish_images/clownfish.jpg", "rb") as img_file:
        binary = img_file.read()

    cur = con.cursor()
    cur.execute(
        "INSERT INTO sealife.sealife_data (name, description, image) VALUES (%s, %s, %s)",
        ('clown fish', 'I live in an anemone', psycopg2.Binary(binary)))

    con.commit()
    cur.close()
    return binary


con = db_connection()
insert_data()
con.close()

db_connection()
