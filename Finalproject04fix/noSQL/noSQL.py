from flask import Flask, render_template, request, redirect, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# 連接到 MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['course_database']
courses_collection = db['courses']
selection_history_collection = db['selection_history']

# 初始化資料
def initialize_data():
    courses_collection.delete_many({})
    sample_courses = [
        {"name": "Python 基礎", "college": "理學院", "department": "資訊工程學系"},
        {"name": "資料結構與演算法", "college": "理學院", "department": "資訊工程學系"},
        {"name": "作業系統概論", "college": "理學院", "department": "資訊工程學系"},
        {"name": "人工智慧導論", "college": "理學院", "department": "資訊工程學系"},
        {"name": "計算機組織與設計", "college": "理學院", "department": "資訊工程學系"},
        {"name": "高等數學", "college": "理學院", "department": "數學系"},
        {"name": "線性代數", "college": "理學院", "department": "數學系"},
        {"name": "常微分方程", "college": "理學院", "department": "數學系"},
        {"name": "機率論", "college": "理學院", "department": "數學系"},
        {"name": "數理邏輯", "college": "理學院", "department": "數學系"},
        {"name": "經典力學", "college": "理學院", "department": "物理學系"},
        {"name": "量子力學", "college": "理學院", "department": "物理學系"},
        {"name": "電磁學", "college": "理學院", "department": "物理學系"},
        {"name": "熱力學與統計物理", "college": "理學院", "department": "物理學系"},
        {"name": "固態物理", "college": "理學院", "department": "物理學系"},
        {"name": "教育心理學", "college": "教育學院", "department": "教育學系"},
        {"name": "學習與教學理論", "college": "教育學院", "department": "教育學系"},
        {"name": "課程設計與發展", "college": "教育學院", "department": "教育學系"},
        {"name": "教學評量與回饋", "college": "教育學院", "department": "教育學系"},
        {"name": "教育社會學", "college": "教育學院", "department": "教育學系"},
        {"name": "特殊教育概論", "college": "教育學院", "department": "特殊教育學系"},
        {"name": "行為管理", "college": "教育學院", "department": "特殊教育學系"},
        {"name": "語言發展與障礙", "college": "教育學院", "department": "特殊教育學系"},
        {"name": "特殊需求學生的教育", "college": "教育學院", "department": "特殊教育學系"},
        {"name": "特殊教育法律與政策", "college": "教育學院", "department": "特殊教育學系"},
        {"name": "國際關係", "college": "教育學院", "department": "國際事務學系"},
        {"name": "全球化與發展", "college": "教育學院", "department": "國際事務學系"},
        {"name": "國際組織與合作", "college": "教育學院", "department": "國際事務學系"},
        {"name": "跨文化交流", "college": "教育學院", "department": "國際事務學系"},
        {"name": "國際公共政策", "college": "教育學院", "department": "國際事務學系"},
        {"name": "繪畫技法", "college": "藝術學院", "department": "美術學系"},
        {"name": "藝術史概論", "college": "藝術學院", "department": "美術學系"},
        {"name": "雕塑基礎", "college": "藝術學院", "department": "美術學系"},
        {"name": "視覺藝術設計", "college": "藝術學院", "department": "美術學系"},
        {"name": "數位藝術", "college": "藝術學院", "department": "美術學系"},
        {"name": "音樂理論", "college": "藝術學院", "department": "音樂學系"},
        {"name": "音樂歷史", "college": "藝術學院", "department": "音樂學系"},
        {"name": "鋼琴技巧", "college": "藝術學院", "department": "音樂學系"},
        {"name": "管弦樂指揮", "college": "藝術學院", "department": "音樂學系"},
        {"name": "音樂創作", "college": "藝術學院", "department": "音樂學系"},
        {"name": "現代舞技巧", "college": "藝術學院", "department": "舞蹈學系"},
        {"name": "舞蹈創作", "college": "藝術學院", "department": "舞蹈學系"},
        {"name": "舞蹈歷史與理論", "college": "藝術學院", "department": "舞蹈學系"},
        {"name": "舞蹈編排與表演", "college": "藝術學院", "department": "舞蹈學系"},
        {"name": "舞蹈生理學", "college": "藝術學院", "department": "舞蹈學系"},
        {"name": "社會學理論", "college": "社會科學學院", "department": "社會學系"},
        {"name": "社會調查方法", "college": "社會科學學院", "department": "社會學系"},
        {"name": "犯罪學", "college": "社會科學學院", "department": "社會學系"},
        {"name": "性別與社會", "college": "社會科學學院", "department": "社會學系"},
        {"name": "社會變遷", "college": "社會科學學院", "department": "社會學系"},
        {"name": "心理學導論", "college": "社會科學學院", "department": "心理學系"},
        {"name": "發展心理學", "college": "社會科學學院", "department": "心理學系"},
        {"name": "社會心理學", "college": "社會科學學院", "department": "心理學系"},
        {"name": "心理測量", "college": "社會科學學院", "department": "心理學系"},
        {"name": "臨床心理學", "college": "社會科學學院", "department": "心理學系"},
        {"name": "政治學概論", "college": "社會科學學院", "department": "政治學系"},
        {"name": "國際政治", "college": "社會科學學院", "department": "政治學系"},
        {"name": "比較政治學", "college": "社會科學學院", "department": "政治學系"},
        {"name": "台灣政治", "college": "社會科學學院", "department": "政治學系"},
        {"name": "公共政策分析", "college": "社會科學學院", "department": "政治學系"},
        {"name": "國際行銷", "college": "商學院", "department": "國際企業學系"},
        {"name": "跨文化管理", "college": "商學院", "department": "國際企業學系"},
        {"name": "全球戰略", "college": "商學院", "department": "國際企業學系"},
        {"name": "國際財務管理", "college": "商學院", "department": "國際企業學系"},
        {"name": "國際貿易", "college": "商學院", "department": "國際企業學系"},
        {"name": "財務管理", "college": "商學院", "department": "財務金融學系"},
        {"name": "公司理財", "college": "商學院", "department": "財務金融學系"},
        {"name": "投資學", "college": "商學院", "department": "財務金融學系"},
        {"name": "風險管理", "college": "商學院", "department": "財務金融學系"},
        {"name": "金融市場", "college": "商學院", "department": "財務金融學系"},
        # (添加其他資料，按需擴充)
    ]
    courses_collection.insert_many(sample_courses)

initialize_data()

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
    selection_history_collection.insert_one(data)
    return jsonify({"message": "Selection saved!"})

@app.route('/selection_result')
def selection_result():
    history = list(selection_history_collection.find({}, {"_id": 1, "userName": 1, "courses": 1}))
    return render_template('selection_result.html', history=history)

@app.route('/delete_course', methods=['POST'])
def delete_course():
    data = request.json
    selection_id = data.get("id")
    course_to_delete = data.get("course")
    selection_history_collection.update_one(
        {"_id": selection_id},
        {"$pull": {"courses": course_to_delete}}
    )
    return jsonify({"message": "Course deleted!"})

if __name__ == '__main__':
    app.run(debug=True)
