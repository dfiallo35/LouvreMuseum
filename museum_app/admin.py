from django.contrib import admin
from .models import *

class ArtworkAd(admin.ModelAdmin):
    list_display = ('name', 'type', 'author', 'period', 'creation_date', 'economic_valuation', 'entry_date', 'image', 'state')

class StateAd(admin.ModelAdmin):
    list_display = ('artwork',)

class PaintingAd(admin.ModelAdmin):
    list_display = ('name', 'technique', 'style')

class SculptureAd(admin.ModelAdmin):
    list_display = ('name', 'material', 'style')

class CollaboratingMuseumAd(admin.ModelAdmin):
    list_display = ('name',)

class GivenAd(admin.ModelAdmin):
    list_display = ('collaborating_museum', 'given_time', 'amount_received')

class RestorationAd(admin.ModelAdmin):
    list_display = ('restoration_type', 'start_date', 'finish_date')


admin.site.register(Artwork, ArtworkAd)
admin.site.register(State, StateAd)
admin.site.register(Painting, PaintingAd)
admin.site.register(Sculpture, SculptureAd)
admin.site.register(CollaboratingMuseum, CollaboratingMuseumAd)
admin.site.register(Given, GivenAd)
admin.site.register(Restoration, RestorationAd)