from database import connect


def add_task(task, user_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks(task, done, user_id) VALUES (?, ?, ?)",
        (task, 0, user_id)
    )

    conn.commit()
    conn.close()
