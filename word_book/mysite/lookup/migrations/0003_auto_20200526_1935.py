# Generated by Django 3.0.6 on 2020-05-26 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lookup', '0002_auto_20200526_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='definition',
            field=models.TextField(null=True),
        ),
    ]
