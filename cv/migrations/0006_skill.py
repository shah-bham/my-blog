# Generated by Django 2.2.15 on 2020-08-31 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0005_auto_20200831_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.CV')),
            ],
        ),
    ]