# Generated by Django 4.1.7 on 2023-03-10 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_exam_general_instruction'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_exam_master',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
