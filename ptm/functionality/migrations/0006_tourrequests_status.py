# Generated by Django 2.2.3 on 2020-02-05 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('functionality', '0005_auto_20200205_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourrequests',
            name='status',
            field=models.CharField(blank=True, choices=[('In Creation', 'In Creation'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='In Creation', max_length=20),
        ),
    ]
