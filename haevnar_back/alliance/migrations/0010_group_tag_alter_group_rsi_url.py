# Generated by Django 5.0.2 on 2024-03-03 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alliance', '0009_remove_group_approved_group_type_alter_group_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='tag',
            field=models.CharField(default='LESHOMIES', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='rsi_url',
            field=models.URLField(default='https://robertsspaceindustries.com/orgs/LESHOMIES'),
            preserve_default=False,
        ),
    ]