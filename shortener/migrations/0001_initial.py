# Generated by Django 4.2.3 on 2023-07-25 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLItem',
            fields=[
                ('reference', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('url', models.URLField(unique=True)),
            ],
        ),
    ]
