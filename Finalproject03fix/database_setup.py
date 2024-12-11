from pymongo import MongoClient

# 連接 MongoDB
client = MongoClient('mongodb://localhost:27017/')  # 確保伺服器運行在本機

# 創建資料庫與集合
db = client['course_database']  # 資料庫名稱
courses_collection = db['courses']  # 集合名稱

# 插入課程數據
courses = [
    {
        "name": "教育心理學",
        "college": "教育學院",
        "department": "教育心理與輔導學系",
        "degree": "學士班",
        "semester": "上學期",
        "weekday": "Monday",
        "time": "Morning",
        "courseType": "必修",
        "description": "探討心理學在教育中的應用。"
    },
    {
        "name": "資訊工程導論",
        "college": "理學院",
        "department": "資訊工程學系",
        "degree": "學士班",
        "semester": "下學期",
        "weekday": "Wednesday",
        "time": "Afternoon",
        "courseType": "選修",
        "description": "了解資訊工程的基本概念。"
    },
    {
        "name": "視覺設計基礎",
        "college": "藝術學院",
        "department": "設計學系",
        "degree": "學士班",
        "semester": "上學期",
        "weekday": "Friday",
        "time": "Morning",
        "courseType": "選修",
        "description": "學習視覺設計的基礎理論與實作技巧。"
    }
]

# 清空集合並插入新的課程數據
courses_collection.delete_many({})  # 清空集合
courses_collection.insert_many(courses)  # 插入資料

print("課程數據已成功插入！")
