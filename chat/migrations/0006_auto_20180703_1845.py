# Generated by Django 2.0.6 on 2018-07-03 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_auto_20180702_1218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problem',
            old_name='answer',
            new_name='ques_answer',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='room',
        ),
        migrations.AddField(
            model_name='room',
            name='max',
            field=models.IntegerField(default=0),
        ),
    ]