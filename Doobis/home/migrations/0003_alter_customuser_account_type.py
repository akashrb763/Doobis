# Generated by Django 5.0.2 on 2024-03-14 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_customuser_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='account_type',
            field=models.CharField(choices=[('Bussiness Buyer', 'Bussiness Buyer'), ('Bussiness Invester', 'Bussiness Invester'), ('Doobiz Franchaise', 'Doobiz Franchaise')], max_length=20),
        ),
    ]