# Generated by Django 4.2 on 2023-07-04 20:26

import IFCuida.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adm', '0002_questaoformsaude_respostaquestaoformsaude'),
        ('aluno', '0003_vacinasadicionadas_motivo_rejeicao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacinasadicionadas',
            name='comprovante',
            field=models.ImageField(upload_to=IFCuida.utils.GeradorNomeArquivo.gerar),
        ),
        migrations.CreateModel(
            name='RespostaSelecionadaFormSaude',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adm.respostaquestaoformsaude')),
                ('usuario_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
