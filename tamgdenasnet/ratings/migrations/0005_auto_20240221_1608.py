# Generated by Django 2.2.19 on 2024-02-21 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0004_auto_20240211_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Climate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField()),
                ('value', models.FloatField()),
                ('year', models.PositiveSmallIntegerField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='climate', to='ratings.Country')),
            ],
        ),
        migrations.AddConstraint(
            model_name='climate',
            constraint=models.UniqueConstraint(fields=('country', 'year'), name='unique_country_year'),
        ),
    ]