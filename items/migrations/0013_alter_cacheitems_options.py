# Generated by Django 3.2 on 2022-12-21 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0012_remove_item_recent_average'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cacheitems',
            options={'verbose_name': '商品', 'verbose_name_plural': '値段蓄積マスタ'},
        ),
    ]
