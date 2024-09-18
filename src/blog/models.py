from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
  # 外部キーの作成と削除方式（カスケード）
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
  title = models.CharField(max_length = 200)
  text = models.TextField()
  careate_date = models.DateTimeField(default = timezone.now)
  publish_date = models.DateTimeField(blank = True, null = True)
  
  def publish(self):
    print('timezone:::', timezone.now())
    self.publish_date = timezone.now()
    self.save()

  def __str__(self):
      return self.title
  