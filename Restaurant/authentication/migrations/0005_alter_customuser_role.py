# Generated by Django 4.2.1 on 2023-05-03 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_rename_refresh_token_customuser_refresh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.IntegerField(choices=[(0, 'Employee'), (1, 'Admin')], default=0),
        ),
    ]
