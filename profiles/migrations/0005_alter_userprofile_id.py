# Generated by Django 3.2 on 2022-02-08 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_userprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
