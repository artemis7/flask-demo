# -*- coding: utf-8 -*-

# 本文件为数据库实体类

from sqlalchemy import Column, Integer, String
from kk import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

    def keys(self):
        return ['id', 'username', 'email']

    def __getitem__(self, item):
        return getattr(self, item)