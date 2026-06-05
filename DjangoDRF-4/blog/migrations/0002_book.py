# Generated manually to add the Book model.

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200)),
                ("text", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
    ]