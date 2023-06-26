# Generated by Django 4.2.2 on 2023-06-19 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0003_registermodel_otp_alter_registermodel_confirm_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registermodel',
            name='otp',
        ),
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.IntegerField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='restapp.registermodel')),
            ],
        ),
    ]
