# Generated by Django 5.0.1 on 2024-01-13 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_project_bookmarks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='bookmarks',
            new_name='bookmarked_users',
        ),
        migrations.RemoveField(
            model_name='project',
            name='likes',
        ),
        migrations.AddField(
            model_name='project',
            name='liked_users',
            field=models.ManyToManyField(related_name='liked_projects', to='app.user'),
        ),
    ]