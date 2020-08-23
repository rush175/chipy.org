# Generated by Django 2.2.12 on 2020-07-30 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_userprofile_is_external_recruiter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_external_recruiter',
            field=models.BooleanField(default=False, verbose_name='Is this posting from a recruiting agency?'),
        ),
    ]