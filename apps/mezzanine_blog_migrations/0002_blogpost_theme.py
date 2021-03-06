# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0004_theme_font_size'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='theme',
            field=models.ForeignKey(blank=True, to='blogging.Theme', null=True),
            preserve_default=True,
        ),
    ]
