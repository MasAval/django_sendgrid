# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('local_sendgrid', '0007_auto_20170616_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactionalemail',
            name='recipient',
        ),
    ]
