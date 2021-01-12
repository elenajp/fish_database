import psycopg2

def db_connection():
    try:
        con = psycopg2.connect(
            host = 'localhost',
            dbname = 'postgres',
            user = 'postgres',
            password = 'passwordd',
            port = '5432')
        print('You have connected to the db')
        return con
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return False

    con.close()

db_connection()
