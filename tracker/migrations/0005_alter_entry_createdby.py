# Generated by Django 4.2.6 on 2023-10-19 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_entry_type_alter_entry_priority_alter_entry_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='createdBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='tracker.user'),
        ),
    ]