# Generated by Django 4.1.1 on 2022-09-21 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tlb_historia',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('id_paciente', models.IntegerField()),
                ('sugerencia', models.CharField(max_length=200)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
