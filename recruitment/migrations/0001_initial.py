# Generated by Django 3.1.4 on 2020-12-10 22:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tsync_id', models.CharField(blank=True, max_length=256, null=True)),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=256)),
                ('phone', models.CharField(max_length=14)),
                ('full_address', models.TextField(blank=True, max_length=512, null=True)),
                ('name_of_university', models.CharField(max_length=256)),
                ('graduation_year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2015), django.core.validators.MaxValueValidator(2020)])),
                ('cgpa', models.DecimalField(decimal_places=2, default=2.0, max_digits=4, validators=[django.core.validators.MinValueValidator(2.0), django.core.validators.MaxValueValidator(4.0)])),
                ('experience_in_months', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('current_work_place_name', models.CharField(blank=True, max_length=256, null=True)),
                ('applying_in', models.CharField(max_length=20)),
                ('expected_salary', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(15000), django.core.validators.MaxValueValidator(60000)])),
                ('field_buzz_reference', models.CharField(blank=True, max_length=256, null=True)),
                ('github_project_url', models.CharField(max_length=512, validators=[django.core.validators.URLValidator])),
                ('cv_file_token_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_id', models.CharField(blank=True, max_length=256, null=True)),
                ('file', models.FileField(upload_to='uploads/%Y/%m/%d/')),
            ],
        ),
    ]