import unittest

from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Projects, UserStories
from os import getenv

class TestBase(TestCase):

	def create_app(self):
		config_name = 'testing'
		app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
				SECRET_KEY=getenv('TEST_SECRET_KEY'),
				WTF_CSRF_ENABLED=False,
				DEBUG=True
				)
		return app

	def setUp(self):
		db.session.commit()
		db.drop_all()
		db.create_all()

		project = Projects(projectName = "Test Project")

		userstory = UserStories(userstoryName = "Test Story", userstoryDesc = "Test Desc", projectident = 1)

		db.session.add(project)
		db.session.add(userstory)
		db.session.commit()

	def tearDown(self):
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

	def test_project_add_page(self):
		with self.client:
			response = self.client.get(url_for('addproject'))
			self.assertIn(b"Create", response.data)

	def test_userstory_view(self):
		with self.client:
			response = self.client.get(url_for('viewuserstories'))
			self.assertIn(b"Test Story", response.data)

	def test_adding_project(self):
		with self.client:
			response = self.client.post(url_for('addproject'), data=dict(projectName = "New Project"), follow_redirects=True)
			self.assertIn(b"New Project", response.data)

	def test_update_project(self):
		with self.client:
			response = self.client.post(('/updateproject/1'), data=dict(projectName = "Retest"), follow_redirects=True)
			self.assertIn(b"Retest", response.data)
			self.assertNotIn(b"Test Project", response.data)

	def test_update_userstory(self):
		with self.client:
			response = self.client.post(('/updateuserstory/1'), data=dict(userstoryName = "Two Story", userstoryDesc= "Two Story Desc"), follow_redirects=True)
			self.assertIn(b"Two Story", response.data)
			self.assertNotIn(b"New Story", response.data)

	def test_project_view_access(self):
		response = self.client.get(url_for('viewprojects'))
		self.assertEqual(response.status_code, 200)

	def test_userstory_view_access(self):
		response = self.client.get(url_for('viewuserstories'))
		self.assertEqual(response.status_code, 200)

	def test_adding_userstory(self):
		with self.client:
			response = self.client.post(url_for('adduserstory'), data=dict(userstoryName = "New Story", userstoryDesc= "New Story Desc", userstoryProject="1"), follow_redirects=True)
			self.assertIn(b"New Story", response.data)

	def test_delete_project(self):
		with self.client:
			response = self.client.get('/deleteproject/1')
			self.assertNotIn("Test Project",response.data)

	def test_delete_userstory(self):
		with self.client:
			response = self.client.get('/deleteuserstory/1')
			self.assertNotIn("Test Story",response.data)	