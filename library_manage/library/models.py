from django.db import models


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, unique=True)
    addr = models.CharField(max_length=128, default="北京")


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, null=False, unique=True)
    publisher = models.ForeignKey(to="Publisher", on_delete=models.CASCADE)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, unique=True, null=False)
    # 多对多关联book ,结合(查询和清空)
    book = models.ManyToManyField(to="Book")


# 自定制many to many
# class Many(models.Model):
#     author = models.ForeignKey("Author", on_delete=models.DO_NOTHING)
#     book = models.ForeignKey("Book", on_delete=models.DO_NOTHING)
#
# # 联合唯一索引
#     class Meta:
#         unique_together = [
#             ('author', 'book'),
#         ]
