# Generated by Django 3.0.2 on 2020-02-07 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('out for delivery', 'out for delivery'), ('delivered', 'delivered')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('category', models.CharField(choices=[('Indoor', 'Indoor'), ('outer door', 'outer door')], max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
