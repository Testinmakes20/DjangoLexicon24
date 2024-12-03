# Generated by Django 5.1.3 on 2024-12-03 10:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsApp', '0003_cart_cartitem'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('category', models.CharField(choices=[('custom_cake', 'Custom Cake Request'), ('existing_order', 'Question About Existing Order'), ('other', 'Other Inquiry')], max_length=20)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('province', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('shipping_method', models.CharField(choices=[('standard', 'Standard Shipping'), ('express', 'Express Shipping'), ('pickup', 'In-store Pickup')], default='standard', max_length=50)),
                ('shipping_notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('cake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productsApp.cake')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='productsApp.order')),
            ],
        ),
    ]
