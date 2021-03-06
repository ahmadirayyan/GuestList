# Generated by Django 3.0.8 on 2020-07-12 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('group', models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms')], default='Mr', max_length=5)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('priority', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third')], default='Third', max_length=10)),
                ('inviter', models.CharField(choices=[('Groom', 'Groom'), ('Bride', 'Bride')], default='Groom', max_length=10)),
                ('estimate', models.PositiveIntegerField(default=2)),
            ],
        ),
    ]
