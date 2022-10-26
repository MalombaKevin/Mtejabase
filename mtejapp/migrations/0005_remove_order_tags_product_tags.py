# Generated by Django 4.1.2 on 2022-10-26 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtejapp', '0004_tag_order_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='mtejapp.tag'),
        ),
    ]
