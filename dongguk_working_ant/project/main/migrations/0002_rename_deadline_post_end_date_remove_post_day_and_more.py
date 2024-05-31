# Generated by Django 5.0.6 on 2024-05-28 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='deadline',
            new_name='end_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='day',
        ),
        migrations.AddField(
            model_name='post',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]