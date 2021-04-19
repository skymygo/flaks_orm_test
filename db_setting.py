import pymysql, json

db_info = json.load(open("db_info.json"))
conn = pymysql.connect(
    user=db_info["username"],
    password=db_info["password"],
    host=db_info["host"],
    port=db_info["port"],
    database=db_info["database"],
    charset="utf8"
)

cursor = conn.cursor(pymysql.cursors.DictCursor)

with open("temp_data.csv", encoding="utf-8") as f:
    datas = f.readlines()

datas = [_.rstrip().split(",") for _ in datas[1:]]
datas = [[num+1] + _[0:3] + [_[3].split("|"), _[4].split("|"), _[5].split("|") ]for num,_ in enumerate(datas)]

table_name = "company_tag"

if table_name == "company":
    query = "insert into {} (company_id, company_name) values ".format(table_name)
    insert_data = list()
    for d in datas:
        insert_data.append('({}, "{}")'.format(d[0], d[1] if d[1] else d[2] if d[2] else d[3]))
    query += ", ".join(insert_data)
elif table_name == "language_table":
    query = "insert into {} (language_id, language_type) values ".format(table_name)
    query += ", ".join([
        '(1, "KOR")',
        '(2, "ENG")',
        '(3, "JAP")'
    ])
elif table_name == "company_name":
    query = "insert into {} (company_id, language_id, company_name) values ".format(table_name)
    insert_data = list()
    for d in datas:
        for i in range(1,4):
            if d[i]:
                insert_data.append('({}, {}, "{}")'.format(d[0], i, d[i]))
    query += ", ".join(insert_data)
elif table_name == "company_tag":
    query = "insert into {} (company_id, language_id, company_tag) values ".format(table_name)
    insert_data = list()
    for d in datas:
        for i in range(4,7):
            if len(d[i]) > 0:
                insert_data.extend(['({}, {}, "{}")'.format(d[0],i-3,_) for _ in d[i]])
    query += ", ".join(insert_data)

cursor.execute(query)
conn.commit()