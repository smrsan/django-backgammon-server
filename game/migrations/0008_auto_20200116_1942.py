# Generated by Django 3.0.2 on 2020-01-16 19:42

from django.db import migrations
import game.fields


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_game_invite_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='invite_token',
            field=game.fields.RandomStrField(default='EGukh25kXlJK0rcYCsLaiXqm', max_length=24),
        ),
    ]
