# Generated by Django 2.2.7 on 2020-02-15 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20200212_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='contactNumber',
        ),
    ]
