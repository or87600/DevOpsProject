import itertools
import random
import pymysql
from pypika import Table, Query


def get_connection():
    """
    Establishing a connection to DB
    :return: connection variable
    """
    schema_name = "freedb_OrAntebi"
    conn = pymysql.connect(host='sql.freedb.tech',
                           port=3306,
                           user='freedb_OrAntebi',
                           passwd='$xV@bPezX9@hM@5',
                           db=schema_name)
    return conn


def add_user(user_id, username):
    schema_name = "freedb_OrAntebi"
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_OrAntebi', passwd='$xV@bPezX9@hM@5', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Inserting data into table
    cursor.execute(f"INSERT into {schema_name}.users (name, id) VALUES ('{username}', {user_id})")

    cursor.close()
    conn.close()


def get_user(user_id):
    schema_name = "freedb_OrAntebi"
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_OrAntebi', passwd='$xV@bPezX9@hM@5', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()
    # get all records
    # Inserting data into table
    cursor.execute(f"SELECT id,name FROM {schema_name}.users where id={user_id}")
    user = cursor.fetchall()

    cursor.close()
    conn.close()
    return user


def delete_user(user_id):
    schema_name = "freedb_OrAntebi"
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_OrAntebi', passwd='$xV@bPezX9@hM@5', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()
    # get all records
    # Inserting data into table
    cursor.execute(f"DELETE FROM {schema_name}.users where id={user_id}")

    cursor.close()
    conn.close()
    return user_id


def update_user(user_id, user_name):
    schema_name = "freedb_OrAntebi"
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_OrAntebi', passwd='$xV@bPezX9@hM@5', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()
    # get all records
    # Inserting data into table
    cursor.execute(f"update {schema_name}.users set name={user_name} where id={user_id}")

    cursor.close()
    conn.close()
    return user_id


def get_random_exist_user_id():
    schema_name = "freedb_OrAntebi"
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_OrAntebi', passwd='$xV@bPezX9@hM@5', db=schema_name)
    conn.autocommit(True)

    cursor = conn.cursor()

    # PyPika SELECT
    users = Table("users")
    get_all_users_ids = Query.from_("freedb_OrAntebi.users").select(
        "id"
    )

    get_all_users_ids = get_all_users_ids.get_sql()
    get_all_users_ids = get_all_users_ids.replace('"', '')  # Removing apostrophes from relevant strings

    cursor.execute(get_all_users_ids)
    conn.commit()

    get_db_users_id = []

    # get all users id's from db into list
    for row in cursor:
        get_db_users_id.append(row)

    # clear list of user id's formatting
    get_db_users_id = list(itertools.chain(*get_db_users_id))
    # print("current list from db", get_db_current_users_id)

    try:
        random_exist_user_id = random.choice(get_db_users_id)
        # print("random id:", random_exist_user_id)

    except ValueError as val:
        print(val)
    except UnboundLocalError as localErr:
        print(localErr)
    finally:
        cursor.close()
        conn.close()

    return random_exist_user_id