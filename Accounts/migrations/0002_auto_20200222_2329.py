# Generated by Django 3.0.2 on 2020-02-22 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time_table',
            name='ec',
        ),
        migrations.RemoveField(
            model_name='time_table',
            name='heure_debut',
        ),
        migrations.RemoveField(
            model_name='time_table',
            name='heure_fin',
        ),
        migrations.RemoveField(
            model_name='time_table',
            name='moment',
        ),
        migrations.RemoveField(
            model_name='time_table',
            name='utilisateur',
        ),
        migrations.AddField(
            model_name='time_table',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
