# Generated by Django 4.0.5 on 2022-06-19 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EB_Staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.TextField(max_length=50)),
                ('last_name', models.TextField(max_length=50)),
                ('username', models.TextField(max_length=50, unique=True)),
                ('password', models.TextField(max_length=50)),
                ('confirm_password', models.TextField(max_length=50)),
            ],
        ),
    ]