# Generated by Django 4.1.4 on 2023-03-01 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0004_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='firstname',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastname',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=8),
        ),
    ]
