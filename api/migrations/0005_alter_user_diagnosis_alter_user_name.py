# Generated by Django 4.0.6 on 2022-07-24 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_user_diagnosis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Diagnosis',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='Name',
            field=models.CharField(max_length=50),
        ),
    ]
