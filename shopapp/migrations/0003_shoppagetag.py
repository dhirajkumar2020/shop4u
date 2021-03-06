# Generated by Django 2.2.8 on 2019-12-14 11:35

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('shopapp', '0002_shoppage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopPageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='shopapp.ShopPage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopapp_shoppagetag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
