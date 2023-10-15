# Generated by Django 4.1.7 on 2023-10-14 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sendHomework', '0003_student_delete_homework_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('now_date', models.DateField(auto_now_add=True)),
                ('file', models.FileField(upload_to='homework/')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sendHomework.student')),
            ],
        ),
    ]