# Generated by Django 3.2.2 on 2021-06-05 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0004_auto_20210605_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bag',
            name='user',
        ),
        migrations.DeleteModel(
            name='order',
        ),
        migrations.DeleteModel(
            name='bag',
        ),
    ]