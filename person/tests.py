import datetime

from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase

from person.views import home
from person.models import Person


class HomeTest(TestCase):

    def setUp(self):
        self.request = HttpRequest()
        self.person = Person(
            name='First_name',
            last_name='Last_name',
            dob=datetime.datetime.strptime('01/02/1995', '%m/%d/%Y'),
            bio='some bio info here',
            email='some_email@here.com',
            jid='some@jid.com',
            skype='some_skype',
            other_contact='some other contacts here'
        )
        self.person.save()

    def test_root_url_resolves_to_home(self):
        self.assertEqual(resolve('/').func, home)

    def test_title(self):
        response = home(self.request)
        self.assertIn(
            b'<title>42 Coffee Cups Test Assignment</title>',
            response.content.strip(),
            'Wrong title'
        )

    def test_h2(self):
        response = home(self.request)
        self.assertIn(
            b'<h2>42 Coffee Cups Test Assignment</h2>',
            response.content.strip(),
            'Wrong h2'
        )

    def test_person(self):
        response = home(self.request)
        content = response.content.decode()

        self.assertIn(self.person.name, content)
        self.assertIn(self.person.last_name, content)
        self.assertIn(self.person.dob.strftime('%m/%d/%y'), content)
        self.assertIn(self.person.bio, content)
        self.assertIn(self.person.email, content)
        self.assertIn(self.person.jid, content)
        self.assertIn(self.person.skype, content)
        self.assertIn(self.person.other_contact, content)
