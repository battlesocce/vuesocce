# Generated by Django 2.1.7 on 2020-08-17 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200815_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='team_a',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='belongs', to='app.team'),
        ),
    ]
