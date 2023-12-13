import psycopg2


def get_connection():
    conn = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/postgres")
    return conn


def read_historial(producto=None, fecha=None):
    cursor = get_connection().cursor()
    if producto is not None and fecha is not None:
        cursor.execute(f"SELECT * from api_historial where producto = '{producto}' AND fecha = '{fecha}'")
    else:
        cursor.execute('SELECT * from api_historial')
    return cursor.fetchall()
