# Generated by Django 3.1.7 on 2021-05-19 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0003_auto_20210515_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='difficulty',
            field=models.CharField(choices=[('medium', 'medium'), ('hard', 'hard'), ('easy', 'easy')], max_length=6),
        ),
    ]
