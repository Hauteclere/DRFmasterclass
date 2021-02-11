# Generated by Django 3.0.8 on 2021-02-11 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Climber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specialty', models.CharField(choices=[('S', 'Speed'), ('L', 'Lead'), ('B', 'Boulder')], max_length=1)),
            ],
        ),
    ]
