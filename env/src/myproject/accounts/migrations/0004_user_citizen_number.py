# Generated by Django 3.0 on 2020-02-21 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200217_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='citizen_number',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
