import psycopg2

def run_file(conn_string, sql_file):
    try:
        connection = psycopg2.connect(conn_string)
        cursor = connection.cursor()
        with open(sql_file, 'r') as f:
            lines = f.read().splitlines()
            for line in lines:
                filename = sql_file.replace('fill_all.test.sql', line.replace('\ir ', ''))
                with open(filename, 'r') as sql:
                    cursor.execute(sql.read())
    except (Exception, psycopg2.Error) as error:
        print(error)

