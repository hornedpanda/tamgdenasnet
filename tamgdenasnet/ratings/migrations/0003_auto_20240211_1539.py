# Generated by Django 2.2.19 on 2024-02-11 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_auto_20240131_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(default=0)),
                ('cost_index', models.FloatField()),
                ('year', models.PositiveSmallIntegerField()),
                ('rent_index', models.FloatField()),
                ('cost_rent_index', models.FloatField()),
                ('salary', models.FloatField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cost', to='ratings.Country')),
            ],
        ),
        migrations.AddConstraint(
            model_name='cost',
            constraint=models.UniqueConstraint(fields=('country', 'year'), name='unique_country_year'),
        ),
    ]
