# Generated by Django 5.0.2 on 2024-03-14 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='account_type',
            field=models.CharField(choices=[('Bussiness_Buyer', 'Bussiness_Buyer'), ('Bussiness_Invester', 'Bussiness_Invester'), ('Doobiz_Franchaise', 'Doobiz_Franchaise')], max_length=20),
        ),
    ]
