from django.contrib import admin
from .models import *

class ArtworkAd(admin.ModelAdmin):
    list_display = ('name', 'author', 'period', 'creation_date', 'entry_date', 'economic_valuation')
    search_fields = ['name', 'author', 'period']
    list_filter = ('author', 'period',)

class StateAd(admin.ModelAdmin):
    list_display = ('artwork',)
    search_fields =['artwork']

class PaintingAd(admin.ModelAdmin):
    list_display = ('name', 'author', 'period', 'creation_date', 'entry_date', 'economic_valuation', 'technique', 'style')
    search_fields = ['name', 'technique', 'style']
    list_filter = ('technique', 'style')

class SculptureAd(admin.ModelAdmin):
    list_display = ('name', 'author', 'period', 'creation_date', 'entry_date', 'economic_valuation', 'material', 'style')
    search_fields = ['name', 'material', 'style']
    list_filter = ('material', 'style')

class CollaboratingMuseumAd(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

class GivenAd(admin.ModelAdmin):
    list_display = ('artwork', 'collaborating_museum', 'given_time', 'date_time', 'amount_received', 'state')
    search_fields = ['artwork', 'collaborating_museum']
    list_filter = ('collaborating_museum',)

class RestorationAd(admin.ModelAdmin):
    list_display = ('artwork', 'restoration_type', 'date_time', 'finish_date', 'state')
    search_fields = ['artwork', 'restoration_type']
    list_filter = ('restoration_type',)

class ExibitionAd(admin.ModelAdmin):
    list_display = ('artwork', 'date_time', 'state')
    search_fields = ['artwork']


admin.site.register(Artwork, ArtworkAd)
admin.site.register(State, StateAd)
admin.site.register(Painting, PaintingAd)
admin.site.register(Sculpture, SculptureAd)
admin.site.register(CollaboratingMuseum, CollaboratingMuseumAd)
admin.site.register(Given, GivenAd)
admin.site.register(Restoration, RestorationAd)
admin.site.register(Exibition, ExibitionAd)