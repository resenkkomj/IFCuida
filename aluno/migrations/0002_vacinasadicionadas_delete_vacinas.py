# Generated by Django 4.2 on 2023-06-30 20:54

import IFCuida.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adm', '0001_initial'),
        ('aluno', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VacinasAdicionadas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('comprovante', models.ImageField(upload_to=IFCuida.utils.GeradorNomeArquivo.gerar)),
                ('estado', models.CharField(max_length=50)),
                ('usuario_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vacina_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adm.vacinas')),
            ],
        ),
        migrations.DeleteModel(
            name='Vacinas',
        ),
    ]
