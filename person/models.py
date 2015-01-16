from django.db import models


class Person(models.Model):

    name = models.CharField(max_length=256,)
    last_name = models.CharField(max_length=256,)
    # date of birth
    dob = models.DateField()
    bio = models.TextField(blank=True,)

    email = models.EmailField()
    # jabber id
    jid = models.CharField(max_length=256,)
    skype = models.CharField(max_length=256,)

    other_contact = models.TextField(blank=True,)