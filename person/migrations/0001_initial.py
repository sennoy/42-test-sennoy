# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('dob', models.DateField()),
                ('bio', models.TextField(blank=True)),
                ('email', models.EmailField(max_length=75)),
                ('jid', models.CharField(max_length=256)),
                ('skype', models.CharField(max_length=256)),
                ('other_contact', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
