# Generated by Django 4.1 on 2022-08-24 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='documents/')),
                ('revision', models.IntegerField()),
            ],
        ),
    ]