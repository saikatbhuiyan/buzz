# Generated by Django 3.1.4 on 2020-12-10 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='cv_file_token_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
