# Generated by Django 3.0.7 on 2020-07-01 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0021_auto_20200701_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.State'),
        ),
    ]
