# Generated by Django 2.2 on 2019-09-21 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '图书信息', 'verbose_name_plural': '图书信息'},
        ),
        migrations.AlterModelOptions(
            name='hero',
            options={'verbose_name': '人物信息', 'verbose_name_plural': '人物信息'},
        ),
        migrations.AddField(
            model_name='book',
            name='views',
            field=models.IntegerField(default=0, verbose_name='阅读量'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(verbose_name='出版日期'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=20, verbose_name='书籍名称'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='Book',
            field=models.ForeignKey(on_delete=False, to='bookApp.Book', verbose_name='所属书籍'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='content',
            field=models.CharField(max_length=100, verbose_name='详情'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='gender',
            field=models.BooleanField(verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='name',
            field=models.CharField(max_length=20, verbose_name='姓名'),
        ),
    ]
