from django.db import models


class myblog(models.Model):
    title=models.CharField(max_length=200)
    description= models.TextField()
    date= models.DateField(null=True,blank=False)


    def __str__(self):   #it shows the default name when someone looks at it in the admin db
        return self.title

#no migration has to be made when changes has to be done in admin
