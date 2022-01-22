# Generated by Django 3.2.5 on 2021-08-05 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crypto_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('detail', models.TextField(blank=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='crypto_pics')),
            ],
        ),
    ]
