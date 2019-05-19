import psycopg2
import os

try:
    conn = psycopg2.connect(user="avi", host="127.0.0.1", port="5432", database=os.environ["DB_NAME"])
    cursor = conn.cursor()
    dsn = conn.get_dsn_parameters()
    cursor.execute("Select version();")
    record = cursor.fetchone()
    print(record)

    create_table_query = '''CREATE TABLE %s (ID serial PRIMARY KEY, NAME varchar(30) NOT NULL, PRICE REAL);'''
    cursor.execute(create_table_query,(os.environ['TABLE_NAME'],))
    # conn.commit()
    # print(record)

    # record_to_insert = '''INSERT INTO MOBILE(NAME,PRICE) VALUES(%s,%s) RETURNING ID;'''
    # values_to_insert = ('Samsung Galaxy J7', '7000')
    # id_record = cursor.execute(record_to_insert, values_to_insert)
    # print(id_record)

    # record_to_update = '''Update mobile set Name=%s where ID=%s''';
    # values_to_update = ('Samsung ACE',6)
    # cursor.execute(record_to_update,values_to_update)

    # record_to_delete = '''Delete from mobile where ID=%s;'''
    # values_to_delete = (5,)
    # cursor.execute(record_to_delete,values_to_delete)

    # EXECUTE MANY
    # record_to_insert = '''INSERT INTO MOBILE(NAME,PRICE) VALUES(%s,%s) RETURNING ID;'''
    # values_to_insert = [('one plus 7', '60000'), ('one plus 9', '80000')]
    # cursor.executemany(record_to_insert, values_to_insert)
    # print(cursor.rowcount)
    #
    # records_to_delete = "DELETE from mobile where id>6";
    # cursor.execute(records_to_delete)
    # print('Records deleted => \t', cursor.rowcount)



    conn.commit()

    select_all = 'select * from %s;'
    cursor.execute(select_all,os.environ['TABLE_NAME'])
    records = cursor.fetchall()

    print(records)

except psycopg2.Error as ex:
    print(ex, "\n OK")

finally:
    if conn:
        cursor.close()
        conn.close()
        print('Closed')
