# Generated by Django 5.0.dev20230505072651 on 2023-05-12 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_memory_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='memory',
            name='favourite',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='images',
            name='nameImage',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
