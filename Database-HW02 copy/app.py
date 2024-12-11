from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

db_config = {
    'user': 'root',
    'password': 'qwaszx40413',
    'host': 'localhost',
    'port': '3306',
    'database': 'course_system'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # 取得學院資料
    cursor.execute("SELECT * FROM colleges")
    colleges = cursor.fetchall()

    # 取得課程紀錄
    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()

    if request.method == 'POST':
        # 儲存選課紀錄
        name = request.form['name']
        college = request.form['college']
        department = request.form['department']
        degree = request.form['degree']
        course_name = request.form['course_name']

        insert_query = """
            INSERT INTO course_records (name, college, department, degree, course_name)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (name, college, department, degree, course_name))
        conn.commit()

    cursor.close()
    conn.close()
    return render_template('index.html', colleges=colleges, courses=courses)

@app.route('/delete/<int:record_id>')
def delete(record_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    delete_query = "DELETE FROM course_records WHERE id = %s"
    cursor.execute(delete_query, (record_id,))
    conn.commit()

    cursor.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/preview', methods=['GET'])
def preview():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM course_records")
    course_records = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template('preview.html', course_records=course_records)

if __name__ == '__main__':
    app.run(debug=True)
