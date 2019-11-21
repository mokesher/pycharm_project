from django.db import models


class UserInfo(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name=models.CharField( max_length=32)
    age=models.IntegerField()
    # 与AuthorDetail建立一对一的关系
    authorDetail=models.OneToOneField(to="AuthorDetail",on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AuthorDetail(models.Model):
    birthday=models.DateField()
    telephone=models.BigIntegerField()
    addr=models.CharField( max_length=64)

    def __str__(self):
        return str(self.telephone)


class Publish(models.Model):
    name=models.CharField( max_length=32)
    city=models.CharField( max_length=32)
    email=models.EmailField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField( max_length=32,verbose_name="书名")
    publishDate=models.DateField(verbose_name="发表日期")
    price=models.DecimalField(max_digits=5,decimal_places=2,verbose_name="价格")
    # 与Publish建立一对多的关系,外键字段建立在多的一方
    publish=models.ForeignKey(to="Publish",to_field="id",on_delete=models.CASCADE,verbose_name="出版社")
    # 与Author表建立多对多的关系,ManyToManyField可以建在两个模型中的任意一个，自动创建第三张表
    authors=models.ManyToManyField(to='Author')

    def __str__(self):
        return self.title