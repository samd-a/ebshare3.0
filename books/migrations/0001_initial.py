# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book_title', models.CharField(max_length=100)),
                ('book_author', models.CharField(max_length=60)),
                ('cover', models.CharField(max_length=20)),
                ('alt_text', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=750)),
                ('details', models.CharField(max_length=200)),
            ],
        ),
    ]
