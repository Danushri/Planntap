# Generated by Django 2.2.6 on 2020-03-24 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0009_auto_20200324_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='Image',
            field=models.ImageField(default='static/Mainapp/images/sakura.jpg', upload_to='static/Mainapp/images'),
        ),
    ]
