# Generated by Django 4.2.1 on 2023-05-04 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_customuser_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='email',
            new_name='username',
        ),
    ]