#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sqlalchemy, random
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:root@127.0.0.1/dbtest", encoding='utf-8')
Base = declarative_base()


class Code(Base):
    __tablename__ = 'code'
    id = Column(Integer, primary_key=True)
    activation_code = Column(String(64))

    def __repr__(self):
        return "<id:%s code:%s>" % (self.id, self.activation_code)


Base.metadata.create_all(engine)
Session_class = sessionmaker(bind=engine)
Session = Session_class()


def code_func():
    code_list = []
    num = 1
    while True:
        code = ''
        for i in range(32):
            rnd_ABC = chr(random.randint(65, 90))
            rnd_num = str(random.randint(0, 9))
            code = code + random.choice([rnd_ABC, rnd_num])
        code_list.append(code)
        num += 1

        if num > 10: break
    return code_list


for i in code_func():
    code_obj = Code(activation_code=i)
    Session.add(code_obj)

data = Session.query(Code).filter_by().all()
print(data)
Session.commit()
