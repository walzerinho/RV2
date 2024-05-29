# Generated by Django 5.0.6 on 2024-05-28 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number_of_players', models.IntegerField()),
                ('number_of_games', models.IntegerField()),
                ('format', models.CharField(choices=[('championship', 'Championship'), ('brackets', 'Brackets'), ('swiss_round', 'Swiss Round')], max_length=20)),
            ],
        ),
    ]