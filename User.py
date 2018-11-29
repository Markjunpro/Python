# !/usr/bin/env python2
# -coding:utf-8-*-


from orm import Model ,StringField , IntegerField

class User(Model):
    __table__ = 'users'

    id = IntegerField(primary_key=True)
    name = StingField()

user = User(id =123,name='username')
user.insert()
users = User.findall()
