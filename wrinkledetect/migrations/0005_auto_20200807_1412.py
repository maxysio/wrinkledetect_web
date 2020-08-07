# Generated by Django 3.0.7 on 2020-08-07 14:12

from django.db import migrations, models
import django.db.models.deletion
import wrinkledetect.validators


class Migration(migrations.Migration):

    dependencies = [
        ('wrinkledetect', '0004_imageanalysis_img_anly_fn'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_fn', models.ImageField(null=True, upload_to='upload_img', validators=[wrinkledetect.validators.validate_file_extension], verbose_name='Select Image')),
            ],
        ),
        migrations.RenameField(
            model_name='imageanalysis',
            old_name='seat_serial',
            new_name='img_seat_serial',
        ),
        migrations.RemoveField(
            model_name='imageanalysis',
            name='img_fn',
        ),
        migrations.AddField(
            model_name='imageanalysis',
            name='img_anly_end_time',
            field=models.DateTimeField(auto_now=True, verbose_name='End Time: '),
        ),
        migrations.AddField(
            model_name='imageanalysis',
            name='img_anly_exec_time',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=30, verbose_name='Execution Duration: '),
        ),
        migrations.AddField(
            model_name='imageanalysis',
            name='img_anly_start_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Start Time: '),
        ),
        migrations.AlterField(
            model_name='imageanalysis',
            name='img_analysis_json',
            field=models.TextField(default=None, verbose_name='Analysis JSON'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imageanalysis',
            name='img_anly_fn',
            field=models.ImageField(null=True, upload_to='upload_img', validators=[wrinkledetect.validators.validate_file_extension], verbose_name='Analyzed Image'),
        ),
        migrations.AddField(
            model_name='imageanalysis',
            name='image',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='wrinkledetect.ImageDetails', verbose_name='Input Image: '),
            preserve_default=False,
        ),
    ]