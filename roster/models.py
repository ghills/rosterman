from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length="50")
    
    def __unicode__(self):
        return self.name
        

class Team(models.Model):
    name = models.CharField(max_length="50")
    city = models.ForeignKey(City)
    owner = models.CharField(max_length="100")
    founding_date = models.DateField('Founding Date')
    
    def __unicode__(self):
        return "%s %s" % (self.city, self.name)
    
class Player(models.Model):
    first_name = models.CharField(max_length="50")
    last_name = models.CharField(max_length="50")
    number = models.IntegerField()
    height = models.IntegerField()
    team = models.ForeignKey(Team)
    
    def __unicode__(self):
        return "%s %s" % (self.first_name,self.last_name)
