# Generated by Django 5.0.6 on 2024-06-20 17:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("administracao", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servico",
            name="procentagem_comissao",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name="servico",
            name="valor_banheiro",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name="servico",
            name="valor_cozinha",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name="servico",
            name="valor_minimo",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name="servico",
            name="valor_outros",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name="servico",
            name="valor_quarto",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name="servico",
            name="valor_quintal",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name="servico",
            name="valor_sala",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]