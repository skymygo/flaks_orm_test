from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Company(Base):
    __tablename__ = "company"
    company_id = Column(Integer, primary_key=True)
    company_name = Column(String)

    def __init__(self, company_id, company_name):
        self.company_id = company_id
        self.company_name = company_name

    def __repr__(self):
        return "<Company({}, {})>".format(self.company_id, self.company_name)

class LanguageTable(Base):
    __tablename__ = "language_table"
    language_id = Column(Integer, primary_key=True)
    language_type = Column(String)

    def __init__(self, language_id, language_type):
        self.language_id = language_id
        self.language_type = language_type

    def __repr__(self):
        return "<LanguageTable({}, {})>".format(self.language_id, self.language_type)

class CompanyName(Base):
    __tablename__ = "company_name"
    name_id = Column(Integer, primary_key=True)
    company_id = Column(Integer)
    language_id = Column(Integer)
    company_name = Column(String)

    def __init__(self, name_id, company_id, language_id, company_name):
        self.name_id = name_id
        self.company_id = company_id
        self.language_id = language_id
        self.company_name = company_name

    def __repr__(self):
        return "<CompanyName({}, {}, {}, {})>".format(self.name_id, self.company_id, self.language_id, self.company_name)

class CompanyTag(Base):
    __tablename__ = "company_tag"
    tag_id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer)
    language_id = Column(Integer)
    company_tag = Column(String)

    def __init__(self, tag_id, company_id, language_id, company_tag):
        self.tag_id = tag_id
        self.company_id = company_id
        self.language_id = language_id
        self.company_tag = company_tag

    def __repr__(self):
        return "<CompanyTag({}, {}, {}, {})>".format(self.tag_id, self.company_id, self.language_id, self.company_tag)