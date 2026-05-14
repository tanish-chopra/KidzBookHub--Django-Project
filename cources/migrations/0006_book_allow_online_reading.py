from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('cources', '0005_alter_book_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='allow_online_reading',
            field=models.BooleanField(default=True),
        ),
    ]
