# Generated by Django 3.0 on 2019-12-04 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='cats_photo/')),
            ],
        ),
        migrations.AlterModelOptions(
            name='departments',
            options={'managed': False, 'verbose_name': '부서', 'verbose_name_plural': '부서들'},
        ),
        migrations.AlterModelOptions(
            name='employees',
            options={'managed': False, 'verbose_name': '직원', 'verbose_name_plural': '직원들'},
        ),
    ]
