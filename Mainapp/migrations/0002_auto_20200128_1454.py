# Generated by Django 3.0 on 2020-01-28 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='Eventname',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
