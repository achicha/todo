import unittest

from flask import current_app
from flask_testing import TestCase
from app import create_app

app = create_app()


class TestTestingConfig(TestCase):

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue(app.config['WTF_CSRF_ENABLED'] is False)

    def test_app_exists(self):
        self.assertFalse(current_app is None)


if __name__ == '__main__':
    unittest.main()
