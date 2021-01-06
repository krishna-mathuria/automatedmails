# Generated by Django 3.0.6 on 2021-01-06 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Excel', models.FileField(upload_to='excel/')),
                ('Html', models.FileField(upload_to='templates/')),
                ('Subject', models.CharField(default='Sample', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Address', models.TextField()),
                ('City', models.CharField(max_length=20)),
                ('Zipcode', models.IntegerField()),
                ('Country', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.IntegerField()),
            ],
        ),
    ]