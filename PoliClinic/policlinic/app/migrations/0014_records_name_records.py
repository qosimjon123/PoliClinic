# Generated by Django 5.1.2 on 2024-11-01 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_records_name_records'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='name_records',
            field=models.CharField(default='Запись', max_length=100),
        ),
    ]