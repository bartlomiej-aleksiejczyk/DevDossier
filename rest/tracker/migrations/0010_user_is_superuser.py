# Generated by Django 4.2.6 on 2023-11-29 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0009_alter_user_avatarpath'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
