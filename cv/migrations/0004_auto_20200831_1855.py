# Generated by Django 2.2.15 on 2020-08-31 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_auto_20200831_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='email',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='cv',
            name='full_name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='cv',
            name='mobile_number',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='cv',
            name='personal_profile',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='cv',
            name='website',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
