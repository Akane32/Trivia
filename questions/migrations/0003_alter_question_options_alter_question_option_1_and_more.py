# Generated by Django 5.1.4 on 2024-12-11 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_question_option_1_question_option_2_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['?']},
        ),
        migrations.AlterField(
            model_name='question',
            name='option_1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_3',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_4',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=500),
        ),
    ]
