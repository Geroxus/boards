# Generated by Django 3.0.7 on 2020-07-01 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0020_auto_20200701_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='games.State'),
        ),
    ]
