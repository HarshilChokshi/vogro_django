# Generated by Django 3.0.5 on 2020-05-01 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vogro_api', '0013_delete_complaints'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_complainer_volunteer', models.BooleanField()),
                ('complaint_details', models.TextField(max_length=500)),
                ('client_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vogro_api.ClientUser')),
                ('completed_grocery_post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vogro_api.CompletedGroceryPost')),
                ('volunteer_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vogro_api.VolunteerUser')),
            ],
        ),
    ]
