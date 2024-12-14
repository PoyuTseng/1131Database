from flask import Flask, render_template, request, jsonify, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB連接
client = MongoClient('mongodb://localhost:27017/')
db = client['course_database']
courses_collection = db['courses']
selection_history_collection = db['selection_history']

@app.route('/')
def index():
    colleges = courses_collection.distinct("college")
    return render_template('index.html', colleges=colleges)

@app.route('/get_departments/<college>')
def get_departments(college):
    departments = courses_collection.distinct("department", {"college": college})
    return jsonify(departments)

@app.route('/get_courses/<department>')
def get_courses(department):
    courses = courses_collection.find({"department": department}, {"_id": 0, "name": 1})
    return jsonify([course["name"] for course in courses])

@app.route('/submit_selection', methods=['POST'])
def submit_selection():
    data = request.json
    existing_record = selection_history_collection.find_one({"userName": data["userName"]})
    if existing_record:
        selection_history_collection.update_one(
            {"_id": existing_record["_id"]},
            {"$set": {"courses": data["courses"]}}
        )
    else:
        selection_history_collection.insert_one(data)
    return jsonify({"message": "Selection saved!"})

@app.route('/selection_result')
def selection_result():
    history = list(selection_history_collection.find({}, {"_id": 1, "userName": 1, "courses": 1}))
    return render_template('selection_result.html', history=history)

@app.route('/delete_course', methods=['POST'])
def delete_course():
    data = request.json
    selection_id = ObjectId(data.get("id"))
    course_to_delete = data.get("course")
    
    # 更新選課紀錄，刪除指定的課程
    selection_history_collection.update_one(
        {"_id": selection_id},
        {"$pull": {"courses": course_to_delete}}
    )
    
    # 檢查該使用者的課程是否為空，如果為空則刪除該筆資料
    record = selection_history_collection.find_one({"_id": selection_id})
    if not record['courses']:  # 如果課程數組為空
        selection_history_collection.delete_one({"_id": selection_id})
    
    return jsonify({"message": "Course deleted!"})

@app.route('/edit_course', methods=['POST'])
def edit_course():
    data = request.json
    selection_id = ObjectId(data.get("id"))
    old_course = data.get("oldCourse")
    new_course = data.get("newCourse")
    selection_history_collection.update_one(
        {"_id": selection_id, "courses": old_course},
        {"$set": {"courses.$": new_course}}
    )
    return jsonify({"message": "Course updated!"})

if __name__ == '__main__':
    app.run(debug=True)
