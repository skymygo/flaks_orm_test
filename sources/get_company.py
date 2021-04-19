import json
from flask.views import MethodView
import sqlalchemy as db
from model.data_table import Company, CompanyName, LanguageTable
from sqlalchemy.orm import sessionmaker
from collections import defaultdict


db_info = json.load(open("db_info.json"))
engine = db.create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(
    db_info["username"], db_info["password"], db_info["host"],db_info["port"], db_info["database"]))

Session = sessionmaker(bind=engine)



class SearchCompany(MethodView):

    def __init__(self):
        pass

    def get(self,company):
        res_dict = defaultdict(list)
        with Session() as session:
            for c, l in session.query(CompanyName, LanguageTable). \
                    filter(CompanyName.company_name.like("%{}%".format(company))). \
                    filter(CompanyName.language_id == LanguageTable.language_id).all():
                res_dict[c.company_id].append({"name": c.company_name, "language": l.language_type})
        return json.dumps(res_dict, ensure_ascii=False)
