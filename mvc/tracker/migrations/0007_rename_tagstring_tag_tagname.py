# Generated by Django 4.2.6 on 2023-10-23 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_alter_attachment_createdby_alter_comment_createdby'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tagString',
            new_name='tagName',
        ),
    ]