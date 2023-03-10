# Generated by Django 4.1.7 on 2023-03-07 04:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam_attend_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('login_user', 'login_user'), ('non_login_user', 'non_login_user')], max_length=25, null=True)),
                ('created_dt', models.DateField(auto_now_add=True)),
                ('created_tm', models.TimeField(auto_now_add=True)),
                ('attend_status', models.BooleanField(default=False)),
                ('auth_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Exam_attend_user_auth_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exam_inital_field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateField(auto_now=True)),
                ('updated_dt', models.DateField(null=True)),
                ('created_tm', models.TimeField(auto_now=True)),
                ('updated_tm', models.TimeField(null=True)),
                ('status', models.CharField(max_length=10, null=True)),
                ('title', models.TextField()),
                ('field_type', models.CharField(choices=[('selection', 'selection'), ('Text Input', 'Text Input')], max_length=20, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Main_Exam_Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateField(auto_now=True)),
                ('updated_dt', models.DateField(null=True)),
                ('created_tm', models.TimeField(auto_now=True)),
                ('updated_tm', models.TimeField(null=True)),
                ('status', models.CharField(max_length=10, null=True)),
                ('Exam_title', models.CharField(max_length=50, null=True)),
                ('background_image', models.FileField(null=True, upload_to='exam_background')),
                ('start_message', models.TextField()),
                ('end_message', models.TextField()),
                ('layout', models.CharField(choices=[('0', 'One page with all the questions'), ('1', 'One page per section'), ('2', 'One page per question')], max_length=25, null=True)),
                ('progression_mode', models.CharField(choices=[('Percentage', 'Percentage'), ('Number', 'Number')], max_length=25, null=True)),
                ('Exam_time_limit', models.TimeField(null=True)),
                ('selection_mode', models.CharField(choices=[('All questions', 'All questions'), ('Randomized per section', 'Randomized per section')], max_length=25, null=True)),
                ('scoring_mode', models.CharField(choices=[('0', 'No scoring'), ('1', 'Scoring with answers at the end'), ('2', 'Scoring without answers at the end')], max_length=25, null=True)),
                ('access_mode', models.CharField(choices=[('0', 'Anyone with the link'), ('1', 'Invited people only')], max_length=25, null=True)),
                ('Login_required', models.BooleanField(null=True)),
                ('attempt_limit', models.IntegerField(null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL)),
                ('responsible_person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Main_Exam_Master_auth_id', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Main_Exam_section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateField(auto_now=True)),
                ('updated_dt', models.DateField(null=True)),
                ('created_tm', models.TimeField(auto_now=True)),
                ('updated_tm', models.TimeField(null=True)),
                ('status', models.CharField(max_length=10, null=True)),
                ('section_title', models.CharField(max_length=50, null=True)),
                ('section_type', models.CharField(choices=[('Section', 'Section'), ('Question', 'Question')], max_length=20, null=True)),
                ('Exam_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Main_Exam_section_exam_id', to='app.main_exam_master')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Main_Question_Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateField(auto_now=True)),
                ('updated_dt', models.DateField(null=True)),
                ('created_tm', models.TimeField(auto_now=True)),
                ('updated_tm', models.TimeField(null=True)),
                ('status', models.CharField(max_length=10, null=True)),
                ('Question', models.TextField()),
                ('Imagefield', models.FileField(null=True, upload_to='Question_Bank_image')),
                ('Question_type', models.CharField(choices=[('Radio', 'Multiple choice: only one answer'), ('Checkbox', 'Multiple choice: multiple answers allowed')], max_length=20, null=True)),
                ('Description', models.TextField(null=True)),
                ('manadatory', models.BooleanField(default=False)),
                ('comments', models.CharField(max_length=25, null=True)),
                ('total_mark', models.IntegerField(null=True)),
                ('question_ar', models.TextField(null=True)),
                ('question_en', models.TextField(null=True)),
                ('question_hi', models.TextField(null=True)),
                ('question_ur', models.TextField(null=True)),
                ('question_ta', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Section_Question_Mapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateField(auto_now=True)),
                ('updated_dt', models.DateField(null=True)),
                ('created_tm', models.TimeField(auto_now=True)),
                ('updated_tm', models.TimeField(null=True)),
                ('status', models.CharField(max_length=10, null=True)),
                ('Question_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Question_Bank_id', to='app.main_question_bank')),
                ('Section_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Section_Question_Mapping_id', to='app.main_exam_section')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Role_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateField(auto_now=True)),
                ('updated_dt', models.DateField(null=True)),
                ('created_tm', models.TimeField(auto_now=True)),
                ('updated_tm', models.TimeField(null=True)),
                ('status', models.CharField(max_length=10, null=True)),
                ('role_name', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(null=True)),
                ('auth_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='role_auth_id', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Role_mapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateField(auto_now=True)),
                ('updated_dt', models.DateField(null=True)),
                ('created_tm', models.TimeField(auto_now=True)),
                ('updated_tm', models.TimeField(null=True)),
                ('status', models.CharField(max_length=10, null=True)),
                ('navbar_name', models.CharField(choices=[('User', 'User'), ('Role', 'Role'), ('Exam', 'Exam')], max_length=50, null=True)),
                ('read', models.BooleanField(null=True)),
                ('write', models.BooleanField(null=True)),
                ('edit', models.BooleanField(null=True)),
                ('delete', models.BooleanField(null=True)),
                ('view_all', models.BooleanField(null=True)),
                ('manage_all', models.BooleanField(null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL)),
                ('role_master_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Role_master_role_id', to='app.role_master')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question_Bank_multiple_choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateField(auto_now=True)),
                ('updated_dt', models.DateField(null=True)),
                ('created_tm', models.TimeField(auto_now=True)),
                ('updated_tm', models.TimeField(null=True)),
                ('status', models.CharField(max_length=10, null=True)),
                ('choice', models.CharField(max_length=50, null=True)),
                ('Imagefield', models.FileField(null=True, upload_to='Question_Bank_multiple')),
                ('file_type', models.CharField(max_length=20, null=True)),
                ('Mark', models.IntegerField(null=True)),
                ('result_status', models.BooleanField(default=False)),
                ('choice_ar', models.TextField(null=True)),
                ('choice_en', models.TextField(null=True)),
                ('choice_hi', models.TextField(null=True)),
                ('choice_ur', models.TextField(null=True)),
                ('choice_ta', models.TextField(null=True)),
                ('Question_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Exam_section_exam_id', to='app.main_question_bank')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='main_question_bank',
            name='answer_id',
            field=models.ManyToManyField(blank=True, related_name='Answer_master_id', to='app.question_bank_multiple_choice'),
        ),
        migrations.AddField(
            model_name='main_question_bank',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='main_question_bank',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='main_exam_section',
            name='Question_bank_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Main_Exam_Master_question_id', to='app.main_question_bank'),
        ),
        migrations.AddField(
            model_name='main_exam_section',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='main_exam_section',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Main_exam_language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateField(auto_now=True)),
                ('updated_dt', models.DateField(null=True)),
                ('created_tm', models.TimeField(auto_now=True)),
                ('updated_tm', models.TimeField(null=True)),
                ('status', models.CharField(max_length=10, null=True)),
                ('language_access', models.CharField(choices=[('en', 'English'), ('ar', 'Arabic '), ('ur', 'Urdu'), ('ta', 'Tamil'), ('hi', 'Hindi')], max_length=25)),
                ('Exam_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Main_exam_language_eaxm_id', to='app.main_exam_master')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Exam_inital_field_choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateField(auto_now=True)),
                ('updated_dt', models.DateField(null=True)),
                ('created_tm', models.TimeField(auto_now=True)),
                ('updated_tm', models.TimeField(null=True)),
                ('status', models.CharField(max_length=10, null=True)),
                ('choice_name', models.CharField(max_length=25, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL)),
                ('initial_field_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Exam_inital_field_id', to='app.exam_inital_field')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='exam_inital_field',
            name='Exam_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Exam_inital_field_exam_id', to='app.main_exam_master'),
        ),
        migrations.AddField(
            model_name='exam_inital_field',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='exam_inital_field',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_ownership1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='exam_attend_user_score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mark', models.IntegerField(null=True)),
                ('result_status', models.BooleanField(default=False)),
                ('Question_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exam_attend_user_score_Question_Bank_id', to='app.main_question_bank')),
                ('correct_answer', models.ManyToManyField(related_name='exam_attend_user_score_Question_Bank_id', to='app.question_bank_multiple_choice')),
                ('exam_attend_user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exam_attend_user_score_user_id', to='app.exam_attend_user')),
                ('section_question_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exam_attend_user_score_question_id', to='app.section_question_mapping')),
                ('user_select_choice', models.ManyToManyField(related_name='exam_attend_user_score_Question_Bank_id_select_id', to='app.question_bank_multiple_choice')),
            ],
        ),
        migrations.CreateModel(
            name='exam_attend_user_initial_field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=25, null=True)),
                ('Exam_inital_field_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exam_attend_user_initial_field_id_Exam_inital_field', to='app.exam_inital_field')),
                ('exam_attend_user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exam_attend_user_initial_field_attend_id', to='app.exam_attend_user')),
            ],
        ),
        migrations.AddField(
            model_name='exam_attend_user',
            name='exam_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Exam_attend_user_exam_id', to='app.main_exam_master'),
        ),
        migrations.CreateModel(
            name='customer_answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=50, null=True)),
                ('Mark', models.IntegerField(null=True)),
                ('Exam_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_answers_exam_id', to='app.main_exam_master')),
                ('Question_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_answers_Question_Bank_id', to='app.main_question_bank')),
                ('auth_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
