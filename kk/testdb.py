# -*- coding: utf-8 -*-
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, 
)

from kk import db
from .models import User
import json
from .JSONEncoder import JSONEncoder

bp = Blueprint('testdb', __name__, url_prefix='/testdb')


@bp.route('/create_table', methods=('GET', 'POST'))
def create_table():
    db.drop_all()
    db.create_all()
    res = {}
    res["status"] = "ok"
    res["code"] = 200
    res["description"] = "创建数据库表成功"
    return jsonify(res)


# 只写一个方法时，用()会报错，换成[]就没事
@bp.route('/create_one', methods=['POST'])
def create_one():
    # 拿from表单的参数
    username = request.form.get("username")
    email = request.form.get("email")
    u = User(username, email)
    db.session.add(u)
    db.session.commit()
    res = {}
    res["status"] = "ok"
    res["code"] = 200
    res["description"] = "创建用户成功"
    return jsonify(res)


@bp.route('/query', methods=['get'])
def query():
    # 拿在地址里的参数
    uname = request.args.get("username")
    admin = User.query.filter_by(username=uname).first()
    res = {}
    res["code"] = 200
    if admin == None:
        res["status"] = "fail"
        res["description"] = "查询不到用户"
    else:
        res["status"] = "ok"
        res["description"] = "查询用户成功"
    res["data"] = json.loads(json.dumps(admin, cls=JSONEncoder, ensure_ascii=False));
    return json.dumps(res, ensure_ascii=False)
    
    