from flask import jsonify
from api.models import User
import pprint

class TestUserModel:
  def test_new_user(self, new_user, init_db):
    assert new_user == new_user.save()

  def test_get(self, new_user):
    assert User.get('1') == new_user

  def test_update(self, new_user):
    new_user.update(name='Ayobami')
    assert new_user.name == 'Ayobami' 

  def test_count(self, new_user):
    assert new_user.count()  == 1 

  def test_query(self, new_user):
    user_query = new_user._query()
    assert user_query.count() == 1
    assert isinstance(user_query.all(), list)
    assert user_query.filter_by(name='Ayobami').first() == new_user
    assert user_query.filter(new_user.name == 'Ayobami').count() == 1
    assert isinstance(user_query.filter(new_user.name == 'Ayobami').all(), list)

  def test_delete(self, new_user):
    new_user.delete()
    