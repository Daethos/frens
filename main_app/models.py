from django.db import models
from django.urls import reverse

class Fren(models.Model):
    # name = models.ManyToManyField(Profile)
    nickname = models.CharField(max_length=24)
    first_met = models.DateField()
    favorite_thing = models.TextField(max_length=240)
    super_fren_status = models.BooleanField('Are you two super frens?!', default=True)

    def __str__(self):
        return self.nickname

    def get_absolute_url(self):
        return reverse('detail.fren', kwargs={'pk': self.id})

class Profile(models.Model):
    name = models.CharField(max_length=24)
    age = models.IntegerField()
    description = models.TextField(max_length=240)
    frens = models.ManyToManyField('self', through='Fren')
    fren = models.ManyToManyField(Fren)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail.profile", kwargs={"profile_id": self.id})


class Theme(models.Model):
    name = models.CharField(max_length=48)
    description = models.TextField(max_length=250)
    favorite_color = models.CharField(max_length=24, default='Blue?')
    upload = models.ImageField(upload_to='images/')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name