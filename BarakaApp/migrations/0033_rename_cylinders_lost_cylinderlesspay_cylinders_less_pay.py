# Generated by Django 5.0.7 on 2025-02-03 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BarakaApp', '0032_rename_number_of_cylinder_cylinderlesspay_cylinders_lost_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cylinderlesspay',
            old_name='cylinders_lost',
            new_name='cylinders_less_pay',
        ),
    ]
