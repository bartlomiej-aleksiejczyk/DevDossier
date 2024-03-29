# Generated by Django 4.2.6 on 2023-10-23 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_alter_entry_createdby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='createdBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='tracker.user'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='createdBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tracker.user'),
        ),
    ]
