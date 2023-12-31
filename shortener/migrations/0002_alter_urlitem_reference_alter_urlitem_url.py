# Generated by Django 4.2.3 on 2023-07-25 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlitem',
            name='reference',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='urlitem',
            name='url',
            field=models.URLField(),
        ),
    ]
