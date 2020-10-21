# Generated by Django 3.1.2 on 2020-10-21 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circuit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='uploads/circuits/')),
                ('turns', models.PositiveSmallIntegerField(default=0)),
                ('total_gp', models.PositiveSmallIntegerField(default=0)),
                ('location', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('first_gp_date', models.DateField(blank=True, null=True)),
                ('capacity', models.IntegerField(default=0)),
                ('length', models.FloatField(default=0.0)),
                ('race_lap_record', models.CharField(max_length=50)),
            ],
        ),
    ]