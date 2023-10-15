# Generated by Django 4.1.7 on 2023-10-14 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sendHomework', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='image',
        ),
        migrations.AlterField(
            model_name='homework',
            name='file',
            field=models.FileField(upload_to='homework/'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='now_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
