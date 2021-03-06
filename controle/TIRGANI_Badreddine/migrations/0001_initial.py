# Generated by Django 4.0.4 on 2022-05-09 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomCategorie', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referenceCmd', models.CharField(max_length=45)),
                ('dateCmd', models.DateField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=45)),
                ('prenom', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produitRef', models.CharField(max_length=45)),
                ('nomProduit', models.CharField(max_length=45)),
                ('dateProduit', models.DateField(max_length=45)),
                ('prix', models.FloatField()),
                ('categorie', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Categorie', to='TIRGANI_Badreddine.categorie')),
                ('commande', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Commande', to='TIRGANI_Badreddine.commande')),
            ],
        ),
        migrations.AddField(
            model_name='commande',
            name='personne',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Personne', to='TIRGANI_Badreddine.personne'),
        ),
    ]
