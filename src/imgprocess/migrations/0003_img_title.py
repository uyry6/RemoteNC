# Generated by Django 3.2 on 2021-04-09 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgprocess', '0002_remove_img_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='img',
            name='title',
            field=models.CharField(default='this is title', max_length=20),
        ),
    ]
