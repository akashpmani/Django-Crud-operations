# Generated by Django 4.2 on 2023-04-10 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_user_plain_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='plain_password',
            new_name='plain_pass',
        ),
    ]
