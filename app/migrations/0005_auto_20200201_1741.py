# Generated by Django 3.0.2 on 2020-02-01 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200201_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailer',
            name='subject',
            field=models.CharField(max_length=254),
        ),
    ]
