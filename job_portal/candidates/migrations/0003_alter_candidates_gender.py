# Generated by Django 4.1.4 on 2023-01-29 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_alter_candidates_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidates',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=20),
        ),
    ]
