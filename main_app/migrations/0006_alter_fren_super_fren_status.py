# Generated by Django 4.1 on 2022-09-01 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_fren_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fren',
            name='super_fren_status',
            field=models.BooleanField(default=True),
        ),
    ]
