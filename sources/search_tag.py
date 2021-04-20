import json
from flask.views import MethodView
from flask import request
import sqlalchemy as db
from model.data_table import CompanyName, CompanyTag
from sqlalchemy.orm import sessionmaker
from collections import defaultdict


db_info = json.load(open("db_info.json"))
engine = db.create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(
    db_info["username"], db_info["password"], db_info["host"],db_info["port"], db_info["database"]))

Session = sessionmaker(bind=engine)



class SearchCompanyWithTag(MethodView):

    def __init__(self):
        pass

    def get(self,tag):
        res_dict = defaultdict(list)
        with Session() as session:
            for c, t in session.query(CompanyName, CompanyTag). \
                    filter(CompanyTag.company_tag == tag). \
                    filter(CompanyName.company_id == CompanyTag.company_id).all():
                before_l_id = res_dict.get(c.company_id, dict()).get("l_id", -1)
                if before_l_id != t.language_id and \
                        (before_l_id == -1 or before_l_id > c.language_id or c.language_id == t.language_id):
                    res_dict[c.company_id] = {"l_id": c.language_id, "name": c.company_name}
            name_list = [value.get('name') for key, value in res_dict.items()]
        return json.dumps(name_list, ensure_ascii=False)

class TagManipulation(MethodView):
    def __init__(self):
        pass

    def delete(self, company, tag):
        with Session() as session:
            res = {"error": "삭제하려는 데이터가 존재하지 않습니다."}
            for c, t in session.query(CompanyName, CompanyTag). \
                    filter(CompanyTag.company_tag == tag). \
                    filter(CompanyName.company_id == CompanyTag.company_id).\
                    filter(CompanyName.company_name == company).all():
                session.delete(t)
                res = {"success": "success"}
                session.commit()

        return json.dumps(res, ensure_ascii=False)

    def post(self):
        try:
            data = request.get_data().decode("utf-8")
        except:
            data = request.get_data()
        params = json.loads(data)
        with Session() as session:
            for c, t in session.query(CompanyName, CompanyTag). \
                    filter(CompanyTag.company_tag == params.get("tag")). \
                    filter(CompanyName.company_id == CompanyTag.company_id). \
                    filter(CompanyName.company_name == params.get("company_name")).\
                    filter(CompanyTag.language_id == params.get("language_code")).all():
                res = {"error": "이미 존재하는 데이터입니다."}
                return json.dumps(res, ensure_ascii=False)
            for c in session.query(CompanyName).\
                filter(CompanyName.company_name == params.get("company_name")).all():
                new_tag = CompanyTag(None, c.company_id, params.get("language_code"), params.get("tag"))
                session.add(new_tag)
                session.commit()
                res = {"success": "success"}
                return json.dumps(res, ensure_ascii=False)

        res = {"error":"존재하지 않는 회사입니다."}
        return json.dumps(res, ensure_ascii=False)