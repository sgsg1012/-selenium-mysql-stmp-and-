import pymysql
from test_mail import mail

host = "localhost"
port = 3306
db = "score"
user = "root"
pwd = "shi125515"

list = [{'id': '3350840011023', 'name': '机器学习与模式识别', 'year': '2020-2021', 'sem': '3', 'nature': '专业教育选修', 'credit': '2',
         'score': '93', 'gpa': '4.00', 'class': '20203021779', 'teacher': '许永超', 'credit_gpa': '8.00'},
        {'id': '3150520011091', 'name': '数字逻辑与数字电路设计', 'year': '2020-2021', 'sem': '3', 'nature': '专业教育必修',
         'credit': '1', 'score': '90', 'gpa': '4.00', 'class': '20203021750', 'teacher': '肖忠付', 'credit_gpa': '4.00'},
        {'id': '3350520011047', 'name': '计算机前沿技术1', 'year': '2020-2021', 'sem': '3', 'nature': '专业教育选修', 'credit': '1',
         'score': '94', 'gpa': '4.00', 'class': '20203021759', 'teacher': '蒋晶珏', 'credit_gpa': '4.00'}]


def db_start():
    conn = pymysql.connect(host=host, port=port, db=db, user=user, password=pwd)
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("select id from score")
    id_list = cursor.fetchall()
    # print(id_list)
    return conn, cursor, id_list


def db_handle(cursor, data, id_list):
    if {"id": data['id']} not in id_list:
        instruction = "insert into score values("
        for i in data:
            if i in ("sem", "credit", "score", "gpa", "credit_gpa"):
                instruction += data[i]
            else:
                instruction += "'"
                instruction += data[i]
                instruction += "'"
            instruction += ','
        instruction = instruction[0:-1]
        instruction += ")"
        cursor.execute(instruction)
        # print(instruction)


def db_close(conn, cursor):
    cursor.close()
    conn.commit()
    conn.close()


def mail_data(msg):
    data = ""
    for i in msg:
        tmp = f"{i['name']}    {i['credit']}    {i['score']}    {i['gpa']}\n"
        data = data + tmp
    mail(data)


def handle_data(score):
    conn, cursor, id_list = db_start()
    cursor.execute("select count(*) from score")
    num = cursor.fetchone()
    if (len(score) != num['count(*)']):
        for i in score:
            db_handle(cursor, i, id_list)
        cursor.execute("select count(*) from score")
        num1 = cursor.fetchone()
        if(num!=num1):
            cursor.execute("select year,sem,name,credit,score,gpa from score order by year desc,sem desc")
            msg = cursor.fetchall()
            mail_data(msg)
    db_close(conn, cursor)
