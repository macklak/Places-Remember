# Generated by Django 4.2.1 on 2023-05-30 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memories',
            name='useruid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialaccount.socialaccount'),
        ),
    ]
