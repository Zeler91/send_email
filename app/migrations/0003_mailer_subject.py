# Generated by Django 3.0.2 on 2020-02-01 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_mailer_sended'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailer',
            name='subject',
            field=models.TextField(default='no subject'),
        ),
    ]
