# Generated by Django 4.1.7 on 2023-10-15 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sendHomework', '0004_homework'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='year',
            new_name='grade',
        ),
    ]
