# Generated by Django 3.0 on 2020-03-03 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0005_auto_20200303_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='Image',
        ),
    ]
