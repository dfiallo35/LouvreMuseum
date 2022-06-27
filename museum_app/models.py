from django.db import models
from django.db.models import Model
from datetime import datetime, date, timedelta


class Room(Model):
    name = models.CharField('Room', max_length=100, unique=True)

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Artwork(Model):
    name = models.CharField('Name', max_length=100, unique=True)
    author = models.CharField('Author', max_length=100)
    period = models.CharField('Period', max_length=100)
    economic_valuation = models.PositiveIntegerField('Economic Valuation')
    creation_date = models.PositiveIntegerField('Creation Date', help_text='creation year')
    entry_date = models.DateField('Entry date', auto_now_add=True)
    image = models.ImageField('Image', upload_to="")
    room = models.ForeignKey(Room, verbose_name='Room',
                            on_delete=models.PROTECT,
                            related_name='room',
                            blank=True,
                            null=True)

    class Meta:
        verbose_name = "Artwork"
        verbose_name_plural = "Artworks"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kargs):
        artwork = Artwork.objects.all().filter(id=self.id)
        super().save(*args, **kargs)
        if len(artwork) == 0:   
            new = Exhibition(artwork=self, date_time=datetime.today())
            new.save()


class State(Model):
    artwork = models.ForeignKey(Artwork, verbose_name='Artwork',
                                on_delete=models.CASCADE,
                                related_name='artwork')
    date_time = models.DateTimeField('State Date and Time', auto_now_add=True)

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"
        ordering = ["-date_time"]


#Artwork descendants
class Painting(Artwork):
    technique = models.CharField('Technique', max_length=100, blank=True, null=True)
    style = models.CharField('Style', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Painting"
        verbose_name_plural = "Paintings"
        ordering = ["name"]

class Sculpture(Artwork):
    material = models.CharField('Material', max_length=100, blank=True, null=True)
    style = models.CharField('Style', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Sculpture"
        verbose_name_plural = "Sculptures"
        ordering = ["name"]


class CollaboratingMuseum(Model):
    name = models.CharField('Name', max_length=100, unique=True)

    class Meta:
        verbose_name = "Collaborating Museum"
        verbose_name_plural = "Collaborating Museums"
        ordering = ["name"]

    def __str__(self):
        return self.name


#State descendants
class Loan(State):
    collaborating_museum = models.ForeignKey(CollaboratingMuseum,
                                            on_delete=models.PROTECT,
                                            related_name='Collaborating_museum')
    loan_time = models.PositiveIntegerField('Loan Time', help_text='Loan duration in days')
    amount_received = models.PositiveIntegerField('Amount Received')
    loan_init = models.DateField('Loan Start Date', blank=True, null=True, editable=False)

    class Meta:
        verbose_name = "Loan"
        verbose_name_plural = "Loans"
        get_latest_by = "date_time"
        ordering = ["-date_time"]

    def __str__(self):
        return 'Loan'

class Restoration(State):
    restoration_type = models.CharField('Restoration Type',
                                        max_length=100,
                                        null=True,
                                        blank=True)
    finish_date = models.DateField('Finish Date',
                                    blank=True,
                                    null=True,
                                    editable=False)

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
        verbose_name = "Artwork Currently Under Restoration"
        verbose_name_plural = "Artworks Currently Under Restoration"

class ToRestoration(Artwork):
    class Meta:
        proxy = True
        verbose_name = "Artwork to Restoration"
        verbose_name_plural = "Artworks to Restoration"

class ManagerArtworks(Artwork):
    class Meta:
        proxy = True
        verbose_name = "Economic Value of Artwork"
        verbose_name_plural = "Economic Value of Artworks"

class LoanWaitList(Loan):
    class Meta:
        proxy = True
        verbose_name = "Loan Wait List"
        verbose_name_plural = "Loan Wait List"

    def save(self, *args, **kargs):
        qs= Loan.objects.all().exclude(loan_init=None, id=self.id)
        qsaux= []
        for a in qs:
            if a.loan_init == None or a.loan_init + timedelta(days=a.loan_time) > date.today():
                qsaux.append(a.id)

        if len(qsaux) == 0:
            new = Loan(artwork=self.artwork,
                        date_time=datetime.today(),
                        collaborating_museum=self.collaborating_museum,
                        loan_time=self.loan_time,
                        amount_received=self.amount_received,
                        loan_init=datetime.today())
        else:
            new = Loan(artwork=self.artwork,
                        date_time=datetime.today(),
                        collaborating_museum=self.collaborating_museum,
                        loan_time=self.loan_time,
                        amount_received=self.amount_received)
        new.save()