# Generated by Django 5.0.7 on 2025-01-11 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20250111_1337'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'permissions': [('is_employee', 'Can act as an employee')]},
        ),
    ]
