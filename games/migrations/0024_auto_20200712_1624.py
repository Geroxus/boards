# Generated by Django 3.0.7 on 2020-07-12 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0023_auto_20200703_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='previous',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='games.State'),
        ),
        migrations.AlterField(
            model_name='state',
            name='turn',
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.State')),
            ],
        ),
    ]
