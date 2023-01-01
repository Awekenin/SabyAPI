import psycopg2

host = '192.168.1.31'
user = 'sbisapiuser'
password = 'sbisapi123'
db_name = 'sbis_api_db'
port = 5432

connection = ''

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    # cursor = connection.cursor()

    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT version();'
        )

        print(f'Server version: {cursor.fetchone()}')

except Exception as _ex:
    print(f'[INFO] ERROR {_ex}')
finally:
    if connection:
        # cursor.close()
        connection.close()
        print(f'[INFO] PSQL connection close')

#
# db = sqlite3.connect('Awe')
#
# c = db.cursor()
#
# c.execute()
#
# db.close()