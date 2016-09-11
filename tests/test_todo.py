import unittest

from flask_login import current_user
from flask import request

from base import BaseTestCase
from app.login.models import User
from app.todo_list.models import Post


class TestTodo(BaseTestCase):

    def test_add_new_post(self):
        with self.client:
            # login
            response = self.client.post(
                '/login',
                data=dict(username="admin", password="admin"),
                follow_redirects=True
            )
            self.assertTrue(current_user.name == "admin")
            # add new post
            response1 = self.client.post(
                '/',
                data=dict(text="new_post", author_id=current_user.id),
                follow_redirects=True
            )
            self.assertIn(b'new_post', response1.data)
            # repr
            text = Post.query.filter_by(text='new_post').first()
            self.assertTrue(str(text) == '<title new_post>')


if __name__ == '__main__':
    unittest.main()
