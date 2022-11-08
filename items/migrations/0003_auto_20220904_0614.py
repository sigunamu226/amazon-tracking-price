# Generated by Django 3.2 on 2022-09-04 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20220904_0602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(db_index=True, max_length=300, verbose_name='商品名'),
        ),
        migrations.AlterField(
            model_name='item',
            name='url',
            field=models.CharField(db_index=True, max_length=300, verbose_name='URL'),
        ),
    ]
