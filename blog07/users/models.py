from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    # このOneToOneFieldはユーザー一人一人にという意味である
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
    # こkのupload_toの意味は画像がアップロードされたらそれに変えるという意味、最初はデフォルトの画像


    def __str__(self):
        return f'{self.user.username} Profile'

# f'{}'はprintのようなものである
