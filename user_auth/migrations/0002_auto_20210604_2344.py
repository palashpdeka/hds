# Generated by Django 3.2.2 on 2021-06-04 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('past_records', models.CharField(max_length=100000)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apple', models.IntegerField(default=0)),
                ('potato', models.IntegerField(default=0)),
                ('onion', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='items',
        ),
    ]