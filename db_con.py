import psycopg2

image = open('/Users/elenaperez/Desktop/code/fish_images/clownfish.jpg', 'rb').read()

def db_connection():
    try:
        connection = psycopg2.connect(
            host = 'localhost',
            dbname = 'postgres',
            user = 'postgres',
            password = 'passwordd',
            port = '5432')
        print('You have connected to the db')
        return connection
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return False


def insert_data():
    cur = connection.cursor()
    cur.execute("INSERT INTO sealife.sealife_data (name, description, image) values ('clown fish', 'I live in an anemone', psycopg2.Binary(image) )")

    connection.commit()
    cur.close()


connection = db_connection()
db_connection()
insert_data()
