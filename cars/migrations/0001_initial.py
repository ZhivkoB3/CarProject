# Generated by Django 4.0.4 on 2022-05-24 09:42

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='deleted at')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('soft_delete_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(default=None, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated at')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('soft_delete_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='UserCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('first_reg', models.DateTimeField(auto_now_add=True, verbose_name='first registration')),
                ('odometer', models.IntegerField()),
                ('deleted_at', models.DateTimeField(auto_now=True, null=True, verbose_name='deleted at')),
                ('car_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carbrand')),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carmodel')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('soft_delete_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
