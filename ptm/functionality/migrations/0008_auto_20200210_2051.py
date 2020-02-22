# Generated by Django 2.2.3 on 2020-02-10 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('functionality', '0007_tourrequests_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='area',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='properties',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='tourrequests',
            name='status',
            field=models.CharField(blank=True, choices=[('In Creation', 'In Creation'), ('In Process', 'In Process'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='In Creation', max_length=20),
        ),
    ]
