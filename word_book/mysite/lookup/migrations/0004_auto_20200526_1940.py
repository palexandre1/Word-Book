# Generated by Django 3.0.6 on 2020-05-26 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lookup', '0003_auto_20200526_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='definition',
            field=models.TextField(),
        ),
    ]
