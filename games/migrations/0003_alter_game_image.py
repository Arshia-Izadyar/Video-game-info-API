# Generated by Django 4.2.4 on 2023-08-05 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_remove_company_games_game_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Images'),
        ),
    ]
