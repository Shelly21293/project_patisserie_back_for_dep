# Generated by Django 4.0.6 on 2022-10-23 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_order_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user_name',
        ),
    ]
