from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to ='images/')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title
        
    #object의글번호 self타이틀로 제목 가지게해줌
# Create your models here.
