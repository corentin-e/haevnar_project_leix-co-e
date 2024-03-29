# Generated by Django 5.0.2 on 2024-03-03 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alliance', '0008_group_main_color_group_rsi_url_group_secondary_color_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='approved',
        ),
        migrations.AddField(
            model_name='group',
            name='type',
            field=models.CharField(choices=[('Esc', 'Escouade'), ('Corp', 'Corporation'), ('All', 'Alliance')], default='Corp', max_length=4),
        ),
        migrations.AlterField(
            model_name='group',
            name='status',
            field=models.CharField(choices=[('Att', 'Attente'), ('App', 'Approuve'), ('Rej', 'Rejete')], default='Att', max_length=3),
        ),
    ]
