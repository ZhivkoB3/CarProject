# Generated by Django 4.0.4 on 2022-05-24 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_deleted',
        ),
    ]