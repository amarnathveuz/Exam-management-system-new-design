# Generated by Django 4.1.2 on 2023-03-14 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_customer_answers_mark_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='section_question_mapping',
            name='Exam_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Section_Question_Mapping_exam_id', to='app.main_exam_master'),
        ),
    ]