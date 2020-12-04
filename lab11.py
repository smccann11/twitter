import sqlite3
from flask import Flask, render_template, send_from_directory, request, make_response
app = Flask(__name__)

#6,7,2,3,4?

def is_logged_in(cur, username, password):
    sql = '''
        SELECT username,password FROM users where username=? and password=?;
    '''
    cur.execute(sql, (username,password))
    rows = cur.fetchall()

    if len(list(rows))==0:
        return False
    else:
        return True

@app.route('/')
def root():
    con = sqlite3.connect('twitter_clone.db')
    cur = con.cursor()
    sql = '''
        SELECT sender_id,message,created_at,id FROM messages;
    '''
    cur.execute(sql)
    rows = cur.fetchall()
    messages = []
    for row in rows:
        sql = '''
            SELECT username FROM users WHERE id=?
        '''
        cur.execute(sql, (row[0],))
        username_rows = cur.fetchall()
        for username_row in username_rows:
            username = username_row[0]
        messages.append({
            'text' : row[1],
            'username' : username,
            'created_at' : row[2],
            'id' : row[3],
        })

    con = sqlite3.connect('twitter_clone.db')
    cur = con.cursor()
    
    login_successful = is_logged_in(
        cur=cur,
        username=request.cookies.get('username'),
        password=request.cookies.get('password'),
    )

    if login_successful:
        return render_template(
            'root.html',
            username=request.cookies.get('username'),
            messages=messages
            )
    else:
        return render_template(
            'root.html',
            messages=messages
            )



@app.route('/login', methods=['get','post'])
def login():
    if request.form.get('username'):
        con = sqlite3.connect('twitter_clone.db')
        cur = con.cursor()
        login_successful = is_logged_in(
            cur=cur,
            username=request.form.get('username'),
            password=request.form.get('password'),
        )
        """
        sql = '''
            SELECT username,password FROM users where username=? and password=?;
        '''
        cur.execute(sql, (request.form.get('username'), request.form.get('password')))
        rows = cur.fetchall()
        if len(list(rows))==0:
            login_successful=False
        else:
            login_successful=True
            """

        if login_successful:
            res = make_response(render_template(
                'login.html',
                login_successful=True,
                username=request.form.get('username')
                ))
            res.set_cookie('username',request.form.get('username'))
            res.set_cookie('password',request.form.get('password'))
            return res
        else:
            return render_template(
                'login.html',
                login_unsuccessful=True
                )
    else:
        return render_template(
                'login.html',
                login_default=True
                )


@app.route('/logout')
def logout():
    res = make_response(render_template(
        'logout.html',
        ))
    res.set_cookie('username','',expires=0)
    res.set_cookie('password','',expires=0)
    return res

@app.route('/delete_user')
def delete_user(username):
    if request.cookies.get('username'):
        con =sqlite3.connect('twitter_clone.db')
        cur = con.cursor()
        sql="""
        DELETE FROM users WHERE username=?;
        """
        cur.execute(sql, (username,))
        con.commit()
        return render_template('login.html')

@app.route('/delete_message/<id>')
def delete_message(id):
    con = sqlite3.connect('twitter_clone.db')
    cur = con.cursor()
    if is_logged_in(
        cur=cur,
        username=request.cookies.get('username'),
        password=request.cookies.get('password'),
    ):
        sql="""
        DELETE FROM messages WHERE id=?;
        """
        cur.execute(sql, (id,)),
        con.commit(),
        return 'message deleted'

@app.route('/user/<username>')
def user(username):
    return render_template(
        'user.html',
        username=username
        )

@app.route('/static/<path>')
def static_directory(path):
    return send_from_directory('static',path)

@app.route('/create_message', methods=['get', 'post'])
def create_message():
    is_logged_in = True
    if request.form.get('message'):
        con = sqlite3.connect('twitter_clone.db')
        cur = con.cursor()
        sql = """
            SELECT id, username FROM users;
        """
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            if row[1] == request.cookies.get('username'):
                sender_id = row[0]
            print(row)
        message = request.form.get('message')
        con = sqlite3.connect('twitter_clone.db')
        cur = con.cursor()
        sql = """
        INSERT INTO messages (sender_id, message) VALUES (?, ?);
        """
        cur.execute(sql, (sender_id, message))
        con.commit()
        if len(message) == 0:
            message_successful = False
        else:
            message_successful = True

        if message_successful:
            res = make_response(render_template(
                'root.html',
                message_successful = True,
                username = request.cookies.get('username'),
                password = request.cookies.get('password'),
                message = request.cookies.get('message')
            ))
            return res
        else:
            return render_template(
                'create_message.html',
                username = request.cookies.get('username'),
                password = request.cookies.get('password'),
                message_unsuccessful = True
            )
    else:
        res = make_response(render_template(
            'create_message.html',
            username = request.cookies.get('username'),
            password = request.cookies.get('password'),
            message_default = True
        ))
        return res
 
@app.route('/create_user', methods=['get', 'post'])
def create_user():
    if request.method == 'GET':
        return render_template('create_user.html')
    con = sqlite3.connect('twitter_clone.db')
    cur = con.cursor()
    username = request.form.get('username')
    password = request.form.get('password')
    repeatpassword = request.form.get('repeatpassword')
    age = request.form.get('age')

    if password == repeatpassword:
        try:
            sql = """
            INSERT into users (username,password,age) values (?,?,?);
            """
            cur.execute(sql, (username, password, age))
            con.commit()
            return render_template('created.html')
        except sqlite3.IntegrityError:
            return "That username already exists. Please return use a differnet one."
        else:
            return "Passwords don't match! Please return try again."

app.run(host= '0.0.0.0')