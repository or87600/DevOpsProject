import itertools
import json
import random
import requests
import pymysql


def db_conn():
    try:
        schema_name = "freedb_OrAntebi"
        # Establishing a connection to DB
        conn = pymysql.connect(
            host='sql.freedb.tech',
            port=3306,
            user='freedb_OrAntebi',
            passwd='$xV@bPezX9@hM@5',
            db=schema_name
        )

    except pymysql.err.OperationalError as err:
        print(err)

    finally:
        cursor = conn.cursor()
        return cursor, conn


def backend_testing(user_id, user_name):
    url = 'http://127.0.0.1:5000/users/' + str(user_id)

    payload = json.dumps(
        {
            "user_name": user_name
        }
    )
    headers = {
        'Content-Type': 'application/json',
    }
    try:
        #  sending POST with user_id && user_name - from function
        post_res = requests.post(url, data=payload, headers=headers)

        if post_res.ok:
            print(post_res.json())
        else:
            print("Status Code:", post_res.status_code,
                  "Reason: username already exist")
            return

    except requests.exceptions.RequestException as err:
        print(err)

    #  sending GET with user_id - from function

    try:
        get_request = requests.get(url)

        if get_request.ok:
            print("status code:", get_request.status_code,
                  get_request.text)
        else:
            print("status code:", get_request.status_code)
            return

        get_user_id_res = json.loads(get_request.text)
        get_user_id_res = get_user_id_res['user_id']

        # now comparing POST user_id to GET user_id
        if user_id != get_user_id_res:
            raise Exception('User id from POST', user_id, 'is not the same as user_id from GET', get_user_id_res)
        else:
            print('test pass')

    except requests.exceptions.RequestException as err:
        print(err)

    cursor, conn = db_conn()
    schema_name = "freedb_OrAntebi"

    statement_to_exec = f"SELECT id FROM {schema_name}.users WHERE id = {user_id}"

    try:
        cursor.execute(statement_to_exec)
        conn.commit()

        db_user_id = []
        for uid in cursor.fetchall():
            db_user_id.append(uid)

        db_user_id = list(itertools.chain(*db_user_id))
        db_user_id = ', '.join(str(item) for item in db_user_id)

        if user_id != int(db_user_id):
            raise Exception('user_id', user_id, 'is not equal to db_user_id', db_user_id)
        else:
            print('test pass')

    except pymysql.err.IntegrityError as inErr:
        print(inErr)

    finally:
        cursor.close()
        conn.close()


def generate_random_id():
    rand_user_id = random.randint(0, 1000)
    return rand_user_id


def generate_random_name():
    names = [
        'Test-A',
        'Test-B',
        'Test-C'
    ]
    name = random.choice(names)
    return name


backend_testing(generate_random_id(), generate_random_name())
