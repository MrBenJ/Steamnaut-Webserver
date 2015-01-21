# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('video_title', models.CharField(max_length=900)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('video_url', models.CharField(max_length=900)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
