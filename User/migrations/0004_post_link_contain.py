# Generated by Django 3.1.2 on 2020-10-04 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20201002_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link_contain',
            field=models.BooleanField(null=True),
        ),
    ]