import unittest

from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Projects, UserStories
from os import getenv

class TestBase(TestCase):

	def create_app(self):

		# pass in configurations for test database
		config_name = 'testing'
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

		project = Projects(projectName = "Test Project")

		userstory = UserStories(userstoryName = "Test Story", userstoryDesc = "Test Desc", projectident = 1)

		# save users to database
		db.session.add(project)
		db.session.add(userstory)
		db.session.commit()

	def tearDown(self):
		"""
		Will be called after every test
		"""

		db.session.remove()
		db.drop_all()

class TestViews(TestBase):

	def test_homepage_view(self):
		response = self.client.get(url_for('home'))
		self.assertEqual(response.status_code, 200)

	def test_project_view(self):
		with self.client:
			response = self.client.get(url_for('viewprojects'))
			self.assertIn(b"Test Project", response.data)

	def test_userstory_view(self):
		with self.client:
			response = self.client.get(url_for('viewuserstories'))
			self.assertIn(b"Test Story", "Test Desc", response.data)
	