# Generated by Django 5.0.2 on 2024-05-03 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_roles', '0005_delete_userlog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
