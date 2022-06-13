from django.db import models
from django.db.models import Model


class Artwork(Model):
    name = models.CharField('Name', max_length=100)
    author = models.CharField('Author', max_length=100)
    period = models.CharField('Period', max_length=100)
    economic_valuation = models.PositiveIntegerField('Economic Valuation')
    creation_date = models.DateField('Creation Date')
    entry_date = models.DateField('Entry date')
    image = models.ImageField('Image', upload_to="")
    type = models.CharField('Type', max_length=100)

    def __str__(self):
        return self.name


class State(Model):
    artwork = models.OneToOneField(Artwork, on_delete=models.CASCADE, verbose_name='Artwork')
    state = 'Exhibition'

    def __str__(self):
        return self.state

#Artwork descendants
class Painting(Artwork):
    technique = models.CharField('Technique', max_length=100)
    style = models.CharField('Style', max_length=100)

class Sculpture(Artwork):
    material = models.CharField('Material', max_length=100)
    style = models.CharField('Style', max_length=100)


class CollaboratingMuseum(Model):
    name = models.CharField('Name', max_length=100)

    def __str__(self):
        return self.name


#State descendants
class Given(State):
    STATE = [
        ('Given', 'Given'),
    ]
    state_name = models.CharField('State', max_length=20, choices=STATE, editable=True)
    collaborating_museum = models.ForeignKey(CollaboratingMuseum, on_delete=models.CASCADE)
    given_time = models.DurationField('Given time')
    amount_received = models.IntegerField('Amount Received')
    state = 'Given'

class Restoration(State):
    STATE = [
        ('Restoration', 'Restoration'),
    ]
    state_name = models.CharField('State', max_length=20, choices=STATE, editable=True)
    restoration_type = models.CharField('Restoration Type', max_length=100)
    start_date = models.DateField('Start Date')
    finish_date = models.DateField('Finish Date')
    state = 'Restoration'
    

class Exibition(State):
    STATE = [
        ('Exhibition', 'Exhibition')
    ]
    state_name = models.CharField('State', max_length=20, choices=STATE, editable=True)
    state = 'Exhibition'