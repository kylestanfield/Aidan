# Generated by Django 3.0.2 on 2020-01-25 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('filename', models.CharField(max_length=200)),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
                ('id_num', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]