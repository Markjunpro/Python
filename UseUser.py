import orm
from models import User,Blog,Comment

def test():
    yield from orm.create_pool(user='www-data',passwd='www-data',databases='awesome')

    a = User(name='Test',email='test@example.com',passwd='1234567890',image='about :blank')

    yield from u.save()

for x in test():
    pass

