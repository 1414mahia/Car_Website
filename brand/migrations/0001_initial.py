# Generated by Django 5.1.3 on 2024-12-06 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(choices=[('Tesla', 'Tesla'), ('Toyota', 'Toyota'), ('Ferrari', 'Ferrari'), ('Mercedes-Benz', 'Mercedes-Benz'), ('Porsche', 'Porsche'), ('Lamborghini', 'Lamborghini'), ('Rolls-Royce', 'Rolls-Royce'), ('Land Rover', 'Land Rover')], max_length=100)),
            ],
        ),
    ]
