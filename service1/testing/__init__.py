import unittest
from flask import url_for
from os import getenv
from unittest.mock import patch
from flask_testing import TestCase
from application import app,db
from application.models import Team

class TestBase(TestCase):

    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
        SECRET_KEY=getenv('TEST_SECRET_KEY'),
        WTF_CSRF_ENABLED=False,
        DEBUG=True
        )
        return app
    
    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

        # Creating a test team
        testCreature = Team(
            id = 1,
            name = "FC",
            city = "London",
            slogan = "we win"
        )

        # save a team to database
        db.session.add(testCreature)
        db.session.commit()
        

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class Service1Test(TestBase):

    def test_generate_view(self):
        response = self.client.get(url_for("generate_view"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Team Name", response.data)
    
    def test_generate_teams(self):
        with patch('requests.get') as g:
            g.return_value.text = 'London'
            with patch('requests.post') as p:
              p.return_value.text = 'Winners never quit'
              response = self.client.get(url_for("generate_team"))
              self.assertEqual(response.status_code, 200)
              self.assertIn(b"Team Name", response.data)

    def test_view_teams(self):
        response = self.client.get(url_for("home"))
        self.assertEqual(response.status_code, 200)
        print(response.data)
        self.assertIn(b"All Teams", response.data)
        self.assertIn(b"FC", response.data)
        self.assertIn(b"London", response.data)
        self.assertIn(b"we win", response.data)