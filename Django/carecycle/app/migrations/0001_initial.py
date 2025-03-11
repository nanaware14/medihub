# Generated by Django 5.1.6 on 2025-03-11 09:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('Customer', models.CharField(choices=[('customer', 'Customer'), ('admin', 'Admin'), ('pharmacist', 'Pharmacist')], default='customer', max_length=20)),
                ('address', models.TextField(blank=True, null=True)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('medicineid', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('manufacturer', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock_quantity', models.IntegerField()),
                ('expiry_date', models.DateField()),
                ('prescription_required', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(default=None, null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('pincode', models.CharField(max_length=10)),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_addresses', to='app.cuser')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=0)),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.cuser')),
                ('productid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.medicine')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cuser')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal'), ('cod', 'Cash on Delivery')], max_length=20)),
                ('is_successful', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.order')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='prescriptions/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cuser')),
            ],
        ),
    ]
