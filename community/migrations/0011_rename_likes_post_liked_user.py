# Generated by Django 4.2.2 on 2023-06-25 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0010_alter_post_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='likes',
            new_name='liked_user',
        ),
    ]