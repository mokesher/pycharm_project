from django.db import models


# 自关联
class UserInfo(models.Model):
    username = models.CharField(max_length=8)
    password = models.CharField(max_length=8)
    gender_choices = (
        ("男", 1),
        ("女", 2),
    )
    gender = models.IntegerField(choices=gender_choices)

    m = models.ManyToManyField("UserInfo")


class Comment(models.Model):
    news_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=32)
    user = models.CharField(max_length=32)
    reply = models.ForeignKey(to="Comment", on_delete=models.DO_NOTHING, null=True, blank=True)

# class U2U(models.Model):
#     g = models.ForeignKey(to="UserInfo", related_name="boys", on_delete=models.DO_NOTHING)
#     b = models.ForeignKey(to="UserInfo", related_name="girls", on_delete=models.DO_NOTHING)
#     class Meta:
#         unique_together = [
#             ("g", "b")
#         ]
# related_qurry_name
# obj_对象男.girls_set.all()
# obj_对象女.boys_set.all()
# related_name
# obj_对象男.girls.all()
# obj_对象女.boys.all()
