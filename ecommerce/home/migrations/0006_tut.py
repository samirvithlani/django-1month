# Generated by Django 4.1 on 2022-08-31 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_category_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('choice', models.CharField(choices=[('java', 'fs,es,google'), ('php', 'yt,clg'), ('python', 'uni,ech')], max_length=100)),
            ],
        ),
    ]
