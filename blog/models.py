# _*_ encoding: utf-8 _*_
from django.db import models



class Post(models.Model):
    nickname = models.CharField(max_length=10, default='不願意透漏身份的人')
    email = models.EmailField(max_length=70,blank=True, default='和世界失去聯繫的人')
    title = models.CharField(max_length=100, default='這個留言人很懶 沒有標題')
    message = models.TextField(null=False)
    pub_time = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    def __unicode__(self):
        return self.message
