import psycopg2

image = open('/Users/elenaperez/Desktop/code/fish_images/clownfish.jpg', 'rb').read()

def db_connection():
    try:
        connection = psycopg2.connect(
            host = '172.17.0.3',
            dbname = 'fish_images',
            user = 'postgres',
            password = 'passwordd',
            port = '5432')
        print('You have connected to the db')
        return connection
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return False


db_connection()