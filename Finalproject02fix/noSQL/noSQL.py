from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# 連接到 MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['course_database']
courses_collection = db['courses']  # 資料集合

# 初始化資料
def initialize_data():
    courses_collection.delete_many({})  # 清空集合
    sample_courses = [
        {"name": "Python 基礎", "college": "理學院", "department": "資訊工程學系"},
        {"name": "資料結構", "college": "理學院", "department": "資訊工程學系"},
        {"name": "設計概論", "college": "藝術學院", "department": "設計學系"},
        {"name": "創意思考", "college": "藝術學院", "department": "設計學系"}
    ]
    courses_collection.insert_many(sample_courses)

initialize_data()

# 首頁 (階層式選單頁面)
@app.route('/')
def index():
    return render_template('index.html')

# 顯示選課結果頁面
@app.route('/selection_result')
def selection_result():
    return render_template('selection_result.html')

# 課程管理頁面
@app.route('/manage')
def manage():
    courses = list(courses_collection.find({}, {'_id': 0}))
    return render_template('manage.html', courses=courses)

# 新增或刪除課程
@app.route('/delete_course/<string:course_name>', methods=['POST'])
def delete_course(course_name):
    result = courses_collection.delete_one({'name': course_name})
    return {"deleted_count": result.deleted_count}

if __name__ == '__main__':
    app.run(debug=True)
