# Generated by Django 4.0.2 on 2022-02-27 09:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_profile_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='album',
            name='name',
            field=models.CharField(default=-11, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]