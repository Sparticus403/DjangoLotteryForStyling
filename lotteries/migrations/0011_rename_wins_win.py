# Generated by Django 4.0.4 on 2022-05-20 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lotteries', '0010_wins'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Wins',
            new_name='Win',
        ),
    ]