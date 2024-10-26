from flask import Flask, request, render_template, redirect, url_for, session, Blueprint
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your password'
# 創建 Blueprint 實例
delete_bp = Blueprint('delete_bp', __name__)
update_bp = Blueprint('update_bp', __name__)
db_config = {
    'user': 'root',
    'password': 'qwaszx40413',
    'host': 'localhost',
    'port':'3306',
    'database': 'testdb'
}

# 添加 Blueprint 路由
@delete_bp.route('/delete/<int:address_id>', methods=['POST'])
def delete_address(address_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # 刪除指定的地址
    delete_query = "DELETE FROM address WHERE address_id = %s"
    cursor.execute(delete_query, (address_id,))
    conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for('index'))

# 註冊 Blueprint
app.register_blueprint(delete_bp)

@update_bp.route('/update/<int:post_id>', methods=['POST'])
def update_post(post_id):
    # 获取所有字段的新值
    new_address = request.form.get(f'post_{post_id}_address')
    new_address2 = request.form.get(f'post_{post_id}_address2')
    new_district = request.form.get(f'post_{post_id}_district')
    new_city_id = request.form.get(f'post_{post_id}_city_id')
    new_postal_code = request.form.get(f'post_{post_id}_postal_code')
    new_phone = request.form.get(f'post_{post_id}_phone')

    # 检查是否有输入资料，没有的话返回错误
    if not new_address or not new_district or not new_city_id or not new_postal_code or not new_phone:
        return "所有字段都是必需的", 400  # 返回 400 错误，告知缺少必填字段

    # 连接到数据库并更新内容
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    update_query = """
        UPDATE address 
        SET address = %s, address2 = %s, district = %s, city_id = %s, postal_code = %s, phone = %s 
        WHERE address_id = %s
    """
    
    # 执行更新语句
    cursor.execute(update_query, (new_address, new_address2, new_district, new_city_id, new_postal_code, new_phone, post_id))
    conn.commit()  # 提交更改
    
    cursor.close()
    conn.close()
    
    # 更新完成后，重定向到主页
    return redirect(url_for('index'))

app.register_blueprint(update_bp)

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # 初始化或從 session 中獲取上次看到的時間戳
    last_seen_timestamp = session.get('last_seen_timestamp', '1970-01-01 00:00:00')

    if request.method == 'POST':
        # 獲取表單輸入
        address = request.form['address']
        address2 = request.form['address2']
        district = request.form['district']
        city_id = request.form['city_id']
        postal_code = request.form['postal_code']
        phone = request.form['phone']
        location = request.form.get('location', None)

        # 將新記錄插入到資料庫中
        insert_query = """
            INSERT INTO address (address, address2, district, city_id, postal_code, phone, location, last_update)
            VALUES (%s, %s, %s, %s, %s, %s, ST_GeomFromText(%s), NOW())
        """
        cursor.execute(insert_query, (address, address2, district, city_id, postal_code, phone, 'POINT(0 0)' if not location else location))
        conn.commit()

        # 更新 session 中的時間戳（上次更新）
        session['last_seen_timestamp'] = last_seen_timestamp = cursor.lastrowid

    # 查詢自上次看到的時間戳以來新添加的記錄
    select_query = """
        SELECT address_id, address, address2, district, city_id, postal_code, phone, last_update
        FROM address
        WHERE last_update > %s
        ORDER BY last_update DESC
    """
    cursor.execute(select_query, (last_seen_timestamp,))
    new_addresses = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('index.html', addresses=new_addresses)

# 新增城市 ID 搜索功能
@app.route('/search', methods=['GET'])
def search_by_city():
    city_id = request.args.get('city_id')

    if not city_id:
        return "城市ID是必需的", 400  # 返回 400 错误，告知缺少城市 ID

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    search_query = """
        SELECT address_id, address, address2, district, city_id, postal_code, phone, last_update
        FROM address
        WHERE city_id = %s
    """
    cursor.execute(search_query, (city_id,))
    addresses = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('index.html', addresses=addresses)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)