# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webui', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cuckoo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('version', models.CharField(max_length=40)),
            ],
        ),
    ]
