# Generated by Django 4.1.2 on 2022-11-07 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtejapp', '0013_alter_customer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='images/ProfilePic/brain_tech.jpg', null=True, upload_to=''),
        ),
    ]