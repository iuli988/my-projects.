import database_common
from datetime import date


@database_common.connection_handler
def print_questions(cursor):
    query = """
        SELECT id, title, message
        FROM question
        ORDER BY id"""
    cursor.execute(query)
    return cursor.fetchall()

@database_common.connection_handler
def create_registration(cursor, email, password):
    query = f"INSERT INTO account (email, password) VALUES " \
            f"('{email}', '{password}')"
    cursor.execute(query)

@database_common.connection_handler
def print_answers(cursor):
    query = """
        SELECT id, question_id, message
        FROM answer
        ORDER BY question_id"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_questions_by_submission_time(cursor):
    query = """
        SELECT id, submission_time, view_number, vote_number, title, message
        FROM question
        ORDER BY submission_time DESC"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_questions_by_title(cursor):
    query = """
        SELECT id, submission_time, view_number, vote_number, title, message
        FROM question
        ORDER BY title DESC"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_questions_by_view_number(cursor):
    query = """
        SELECT id, submission_time, view_number, vote_number, title, message
        FROM question
        ORDER BY view_number DESC"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_questions_by_vote_number(cursor):
    query = """
        SELECT id, submission_time, view_number, vote_number, title, message
        FROM question
        ORDER BY vote_number DESC"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_questions_by_message(cursor):
    query = """
        SELECT id, submission_time, view_number, vote_number, title, message
        FROM question
        ORDER BY message DESC"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_questions_by_question_id(cursor):
    query = """
        SELECT id, title, message
        FROM question
        ORDER BY message DESC"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def create_question(cursor, title, message):
    query = f"INSERT INTO question ( submission_time, view_number, vote_number, title, message, image) VALUES " \
            f"( '{date.today()}', '0', '0', '{title}', '{message}', 'nothing')"
    cursor.execute(query)


@database_common.connection_handler
def create_answer(cursor, question_id, message):
    query = f"INSERT INTO answer (submission_time, vote_number, question_id, message, image) VALUES " \
            f"( '{date.today()}', '0', '{question_id}', '{message}', 'nothing')"
    cursor.execute(query)


@database_common.connection_handler
def detect_the_question(cursor, question_id):
    query = f"""
        SELECT id, title, message
        FROM question
        WHERE id='{question_id}'"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def detect_the_answer(cursor, question_id):
    query = f"""
        SELECT question_id, message
        FROM answer
        WHERE question_id='{question_id}'"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def like_answer(cursor, question_id):
    query = f"""
        SELECT question_id, vote_number
        FROM answer
        WHERE question_id='{question_id}'"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def like_question(cursor, question_id):
    query = f"""
        SELECT id, vote_number
        FROM question
        WHERE id='{question_id}'"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def search(cursor, term):
    term = term.lower()
    query = f"""
        SELECT message, title
        FROM question
        WHERE lower(title) like '%{term}%' or lower(message) like '%{term}%'
        ORDER BY title DESC"""
    cursor.execute(query)

    return cursor.fetchall()
