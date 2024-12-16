# Generated by Django 5.1.3 on 2024-12-13 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_alter_game_options_rename_date_game_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='question_count',
            field=models.IntegerField(choices=[(10, '10 Preguntas'), (20, '20 Preguntas'), (30, '30 Preguntas'), (40, '40 Preguntas')], default=10),
        ),
    ]
