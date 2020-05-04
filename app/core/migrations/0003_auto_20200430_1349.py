# Generated by Django 3.0.5 on 2020-04-30 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_item_discount_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Item')),
            ],
            options={
                'unique_together': {('item', 'name')},
            },
        ),
        migrations.CreateModel(
            name='ItemVariation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('attachment', models.ImageField(blank=True, upload_to='')),
                ('variation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Variation')),
            ],
            options={
                'unique_together': {('variation', 'value')},
            },
        ),
        migrations.AddField(
            model_name='orderitem',
            name='item_variations',
            field=models.ManyToManyField(to='core.ItemVariation'),
        ),
    ]
