# Generated by Django 4.2.4 on 2023-08-05 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("games", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="company",
            name="games",
        ),
        migrations.AddField(
            model_name="game",
            name="company",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="games",
                to="games.company",
                verbose_name="Company",
            ),
        ),
    ]
