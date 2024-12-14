from flask import Flask, render_template, request, jsonify
import mysql.connector
import json

app = Flask(__name__)

# 連接到 MySQL
db_config = {
    "host": "localhost",
    "user": "root",  # 替換為你的 MySQL 用戶名
    "password": "qwaszx40413",  # 替換為你的 MySQL 密碼
    "database": "course_database"
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

# 初始化資料
def initialize_data():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM courses")  # 清空資料表

    sample_courses = [
        ("Python 基礎", "理學院", "資訊工程學系"),
        ("資料結構與演算法", "理學院", "資訊工程學系"),
        # 添加其他課程資料
    ]
    cursor.executemany(
        "INSERT INTO courses (name, college, department) VALUES (%s, %s, %s)",
        sample_courses
    )
    connection.commit()
    cursor.close()
    connection.close()

initialize_data()

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT DISTINCT college FROM courses")
    colleges = [row["college"] for row in cursor.fetchall()]
    cursor.close()
    connection.close()
    return render_template('index.html', colleges=colleges)

@app.route('/get_departments/<college>')
def get_departments(college):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT DISTINCT department FROM courses WHERE college = %s", (college,))
    departments = [row["department"] for row in cursor.fetchall()]
    cursor.close()
    connection.close()
    return jsonify(departments)

@app.route('/get_courses/<department>')
def get_courses(department):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT name FROM courses WHERE department = %s", (department,))
    courses = [row["name"] for row in cursor.fetchall()]
    cursor.close()
    connection.close()
    return jsonify(courses)

@app.route('/submit_selection', methods=['POST'])
def submit_selection():
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO selection_history (user_name, courses) VALUES (%s, %s)",
        (data["userName"], json.dumps(data["courses"]))
    )
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Selection saved!"})

@app.route('/selection_result')
def selection_result():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT id, user_name, courses FROM selection_history")
    history = [
        {"id": row["id"], "userName": row["user_name"], "courses": json.loads(row["courses"])}
        for row in cursor.fetchall()
    ]
    cursor.close()
    connection.close()
    return render_template('selection_result.html', history=history)

@app.route('/delete_course', methods=['POST'])
def delete_course():
    data = request.json
    selection_id = data.get("id")
    course_to_delete = data.get("course")

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT courses FROM selection_history WHERE id = %s", (selection_id,))
    row = cursor.fetchone()
    if row:
        courses = json.loads(row["courses"])
        if course_to_delete in courses:
            courses.remove(course_to_delete)
            cursor.execute(
                "UPDATE selection_history SET courses = %s WHERE id = %s",
                (json.dumps(courses), selection_id)
            )
            connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Course deleted!"})

if __name__ == '__main__':
    app.run(debug=True)
