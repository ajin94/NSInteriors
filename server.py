import json
from flask import Flask, request
from flask import render_template
from flask import url_for
from flask_wtf.csrf import CsrfProtect
from connections import get_connection
import traceback

app = Flask(__name__)
app.secret_key = '6wfwef6ASDW676w6QDWD6748wd((FD'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['WTF_CSRF_SECRET_KEY'] = 'asdaDa#$@%fewd#22342FWFQE'
csrf = CsrfProtect()
csrf.init_app(app)


@app.route('/')
def index():
    return render_template('client/index.html')


@app.route('/_add_comment', methods=['POST'])
def add_comment():
    name = request.form.get('c_name', None)
    email = request.form.get('c_email', None)
    comment = request.form.get('c_comment', None)
    try:
        cursor, conn = get_connection()
        insert_query = "INSERT INTO comments (name, email, message) VALUES (%s,%s,%s)"
        args = (name, email, comment)
        cursor.execute(insert_query, args)
        conn.commit()
    except Exception as e:
        return json.dumps({"status": "ERROR"})
    else:
        return json.dumps({"status": "OK"})


@app.route('/_add_query', methods=['POST'])
def add_query():
    name = request.form.get('c_name', None)
    email = request.form.get('c_email', None)
    comment = request.form.get('c_query', None)
    try:
        cursor, conn = get_connection()
        insert_query = "INSERT INTO query (name, email, query) VALUES (%s,%s,%s)"
        args = (name, email, comment)
        cursor.execute(insert_query, args)
        conn.commit()
    except Exception as e:
        return json.dumps({"status": "ERROR"})
    else:
        return json.dumps({"status": "OK"})


@app.route('/projects')
def projects():
    template_dict = {}
    image_info_query = "SELECT i.image_name FROM image i INNER JOIN image_category ic ON i.image_for=ic.id where ic.image_for=%s"
    args = ('project gallery',)
    try:
        cursor, conn = get_connection()
        image_info_obj = cursor.execute(image_info_query, args)
        if image_info_obj:
            data = cursor.fetchall()
            temp_list = []
            main_list = []
            if len(data) <= 3:
                main_list = [[file_name for ((file_name,)) in data]]
            else:
                complete_list = [file_name for ((file_name,)) in data]
                while complete_list:
                    file_name = complete_list.pop()
                    temp_list.append(file_name)
                    if len(temp_list) == 3:
                        main_list.append(temp_list)
                        temp_list = []
                if temp_list:
                    main_list.append(temp_list)
                    del temp_list
        template_dict['image_list'] = main_list
    except Exception as e:
        print("exception occurred")
        template_dict['image_list'] = {}

    return render_template('client/projects.html', template_info=template_dict)


@app.route('/testimonials')
def testimonials():
    return render_template('client/testimonials.html')


@app.route('/about')
def about():
    return render_template('client/aboutus.html')


@app.route('/budgetprojects')
def budgetprojects():
    template_dict = {}
    image_info_query = "SELECT i.image_name FROM image i INNER JOIN image_category ic ON i.image_for=ic.id where ic.image_for=%s"
    args = ('budget projects',)
    try:
        cursor, conn = get_connection()
        image_info_obj = cursor.execute(image_info_query, args)
        if image_info_obj:
            data = cursor.fetchall()
            temp_list = []
            main_list = []
            if len(data) <= 3:
                main_list = [[file_name for ((file_name,)) in data]]
            else:
                complete_list = [file_name for ((file_name,)) in data]
                while complete_list:
                    file_name = complete_list.pop()
                    temp_list.append(file_name)
                    if len(temp_list) == 3:
                        main_list.append(temp_list)
                        temp_list = []
                if temp_list:
                    main_list.append(temp_list)
                    del temp_list
        template_dict['image_list'] = main_list
    except Exception as e:
        template_dict['image_list'] = {}
    return render_template('client/budgetprojects.html', template_info=template_dict)


# if __name__ == '__main__':
#     app.run(host='0.0.0.0')
