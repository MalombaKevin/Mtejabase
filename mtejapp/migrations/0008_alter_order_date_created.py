# Generated by Django 4.1.2 on 2022-10-29 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtejapp', '0007_mymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
