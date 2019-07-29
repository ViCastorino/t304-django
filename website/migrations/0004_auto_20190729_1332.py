# Generated by Django 2.2.3 on 2019-07-29 16:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20190726_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ideias',
            old_name='categorias_outros',
            new_name='categoria_outros',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='data_de_criacao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=255, verbose_name='Gênero'),
        ),
    ]