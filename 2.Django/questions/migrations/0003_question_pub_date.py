# Generated by Django 2.1.7 on 2019-03-16 15:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_remove_question_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 16, 15, 10, 3, 346581, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]
