# Generated by Django 5.0.7 on 2024-07-30 10:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('body', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=25)),
                ('members', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.comment')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=18)),
                ('lastname', models.CharField(max_length=30)),
                ('profile_pic', models.FileField(upload_to=None)),
                ('description', models.TextField()),
                ('registered_in', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField()),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.comment')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='group',
            name='posts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.post'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.group'),
        ),
        migrations.AddField(
            model_name='user',
            name='posts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.post'),
        ),
    ]
