from flask import Flask, render_template, request, redirect, session, url_for, escape
import connection

app = Flask(__name__)
questions = connection.print_questions()
answers = connection.print_answers()


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['psw']
        x = connection.create_registration(email, password)
        return redirect('/')

    return render_template("registration.html")

@app.route('/', methods=['GET', 'POST'])
def show_questions():
    if request.method == 'POST':
        user_selected_order = request.form['selected_order']
        if user_selected_order == "submission_time":
            x = connection.get_questions_by_submission_time()
            return render_template("index.html", questions=x, selected=user_selected_order)
        elif user_selected_order == "title":
            x = connection.get_questions_by_title()
            return render_template("index.html", questions=x, selected=user_selected_order)
        elif user_selected_order == "vote_number":
            x = connection.get_questions_by_vote_number()
            return render_template("index.html", questions=x, selected=user_selected_order)
        elif user_selected_order == "view_number":
            x = connection.get_questions_by_view_number()
            return render_template("index.html", questions=x, selected=user_selected_order)
        elif user_selected_order == "message":
            x = connection.get_questions_by_message()
            return render_template("index.html", questions=x, selected=user_selected_order)
        elif user_selected_order == "submission_time":
            x = connection.get_questions_by_submission_time()
            return render_template("index.html", questions=x, selected=user_selected_order)
    else:
        all_questions = connection.print_questions()
        all_answers = connection.print_answers()
        return render_template('index.html', questions=all_questions, all_answers=all_answers)




@app.route('/ask_question', methods=["GET", "POST"])
def ask_question():
    if request.method == 'POST':
        title = request.form['title']
        message = request.form['message']
        x = connection.create_question(title, message)
        return redirect('/')

    return render_template("ask_question.html")


app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))



@app.route('/respond-question/<question_id>', methods=['GET', 'POST'])
def respond_to_question(question_id):
    if request.method == 'POST':
        message = request.form['message']
        x = connection.create_answer(question_id, message)
        return redirect(f'/respond-question/{question_id}')
    question = connection.detect_the_question(question_id)
    answer = connection.detect_the_answer(question_id)
    return render_template('answer.html', question=question, q_id=question_id, answers=answer)


@app.route('/respond-question/<question_id>', methods=['GET', 'POST'])
def like_question(question_id):
    if request.method == 'POST':
        vote_number = request.form['vote_number']
        x = connection.like_question(question_id)
        return redirect('/respond-question/<question_id>')
    question = connection.detect_the_question(question_id)
    answer = connection.detect_the_answer(question_id)
    return render_template('answer.html', question=question, q_id=question_id, answers=answer)


@app.route('/respond-question/<question_id>/<answer_id>', methods=['GET', 'POST'])
def like_answer(question_id):
    if request.method == 'POST':
        vote_number = request.form['vote_number']
        x = connection.like_answer(question_id)
        return redirect('/respond-question/<question_id>')
    question = connection.detect_the_question(question_id)
    answer = connection.detect_the_answer(question_id)
    return render_template('answer.html', question=question, q_id=question_id, answers=answer)


@app.route('/search', methods=['POST'])
def search():
    search_turn = request.form['search']
    results = connection.search(search_turn)
    # return f"{results[0]}"
    return render_template('search.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
