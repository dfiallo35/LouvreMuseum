from django.db import models
from django.db.models import Model
from datetime import datetime

#help_text=


class Room(Model):
    name = models.CharField('Room', max_length=100)

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Artwork(Model):
    name = models.CharField('Name', max_length=100)
    author = models.CharField('Author', max_length=100)
    period = models.CharField('Period', max_length=100)
    economic_valuation = models.PositiveIntegerField('Economic Valuation')
    creation_date = models.DateField('Creation Date')
    entry_date = models.DateField('Entry date')
    image = models.ImageField('Image', upload_to="")
    room = models.ForeignKey(Room, verbose_name='Room',
                            on_delete=models.DO_NOTHING,
                            related_name='room')

    class Meta:
        verbose_name = "Artwork"
        verbose_name_plural = "Artworks"
        ordering = ["name"]

    def __str__(self):
        return self.name


class State(Model):
    artwork = models.ForeignKey(Artwork, verbose_name='Artwork',
                                on_delete=models.CASCADE,
                                related_name='artwork')
    date_time = models.DateTimeField('Date and Time', auto_now_add=True)

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"
        get_latest_by = "date_time"
        ordering = ["-date_time"]


#Artwork descendants
class Painting(Artwork):
    technique = models.CharField('Technique', max_length=100)
    style = models.CharField('Style', max_length=100)

    class Meta:
        verbose_name = "Painting"
        verbose_name_plural = "Paintings"
        ordering = ["name"]

class Sculpture(Artwork):
    material = models.CharField('Material', max_length=100)
    style = models.CharField('Style', max_length=100)

    class Meta:
        verbose_name = "Sculpture"
        verbose_name_plural = "Sculptures"
        ordering = ["name"]


class CollaboratingMuseum(Model):
    name = models.CharField('Name', max_length=100)

    class Meta:
        verbose_name = "Collaborating Museum"
        verbose_name_plural = "Collaborating Museums"
        ordering = ["name"]

    def __str__(self):
        return self.name


#State descendants
class Given(State):
    collaborating_museum = models.ForeignKey(CollaboratingMuseum,
                                            on_delete=models.DO_NOTHING,
                                            related_name='collaborating_museum')
    given_time = models.DurationField('Given time')
    amount_received = models.IntegerField('Amount Received')

    class Meta:
        verbose_name = "Given"
        verbose_name_plural = "Givens"
        get_latest_by = "date_time"
        ordering = ["-date_time"]

    def __str__(self):
        return 'Given'

class Restoration(State):
    restoration_type = models.CharField('Restoration Type', max_length=100)
    finish_date = models.DateField('Finish Date', blank=True, null=True)

    class Meta:
        verbose_name = "Restoration"
        verbose_name_plural = "Restorations"
        get_latest_by = "date_time"
        ordering = ["-date_time"]

    def __str__(self):
        return 'Restoration'

    
    

class Exhibition(State):
    class Meta:
        verbose_name = "Exhibition"
        verbose_name_plural = "Exhibitions"
        get_latest_by = "date_time"
        ordering = ["-date_time"]

    def __str__(self):
        return 'Exhibition'




class CurrentRestoration(Restoration):
    class Meta:
        proxy = True
        verbose_name = "Current Artwok in Restoration"
        verbose_name_plural = "Current Artwoks in Restoration"