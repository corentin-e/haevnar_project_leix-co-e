# Generated by Django 5.0.2 on 2024-02-25 17:58

import discordlogin.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiscordUser',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('avatar', models.CharField(max_length=100)),
                ('public_flags', models.IntegerField(max_length=100)),
                ('flags', models.IntegerField(max_length=100)),
                ('locale', models.CharField(max_length=100)),
                ('mfa_enabled', models.BooleanField()),
                ('last_login', models.DateTimeField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            managers=[
                ('objects', discordlogin.managers.DiscordUserManager()),
            ],
        ),
    ]