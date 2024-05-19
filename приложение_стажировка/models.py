from django.db import models

class User(models.Model):
    login = models.CharField(max_length=20)
    password =  models.CharField(max_length=20)
    fio = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.login


class Question(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    view = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

class FreeDateTime(models.Model):
    datetime = models.DateTimeField()
    user = models.ForeignKey(User, null=True, default=None,blank=True,  on_delete=models.CASCADE)

    def __str__(self):
        return str(self.datetime)



