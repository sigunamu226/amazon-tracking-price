# Generated by Django 3.2 on 2022-12-16 09:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_alter_item_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 9, 56, 14, 753076, tzinfo=utc)),
        ),
    ]
