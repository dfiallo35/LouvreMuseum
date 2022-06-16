from django.contrib import admin
from .models import *


@admin.display(description='Current State',)
def current_state(obj: Artwork):

    states:State = State.objects.filter(artwork__id=obj.id)
    states = states.order_by('-date_time')

    if(len(states) == 0):
        return None
    else:
        states = states[0]

    current_state:Given = Given.objects.filter(id=states.id)
    if len(current_state) != 0:
        return current_state[0]
    
    current_state:Exibition = Exibition.objects.filter(state_ptr=states.id)
    if len(current_state) != 0:
        return current_state[0]
    
    current_state:Restoration = Restoration.objects.filter(state_ptr=states.id)
    if len(current_state) != 0:
        return current_state[0]

    return None


@admin.register(Artwork)
class ArtworkAd(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
        'period',
        'creation_date',
        'entry_date',
        'economic_valuation',
        'room',
        current_state,
    )
    search_fields = [
        'name',
        'author',
        'period',
    ]
    list_filter = (
        'author',
        'period',
    )

    
# @admin.register(State)
# class StateAd(admin.ModelAdmin):
#     list_display = (
#         'artwork',
#         'date_time',
#     )
#     search_fields =[
#         'artwork',
#     ]
#     list_filter=(
#         'artwork',
#     )

@admin.register(Painting)
class PaintingAd(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
        'period',
        'creation_date',
        'entry_date',
        'economic_valuation',
        'technique',
        'style',
        'room',
    )
    search_fields = [
        'name',
        'technique',
        'style',
    ]
    list_filter = (
        'technique',
        'style',
    )

@admin.register(Sculpture)
class SculptureAd(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
        'period',
        'creation_date',
        'entry_date',
        'economic_valuation',
        'material',
        'style',
        'room',
    )
    search_fields = [
        'name',
        'material',
        'style',
    ]
    list_filter = (
        'material',
        'style',
        )

@admin.register(CollaboratingMuseum)
class CollaboratingMuseumAd(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = [
        'name',
    ]

@admin.register(Given)
class GivenAd(admin.ModelAdmin):
    list_display = (
        'artwork',
        'collaborating_museum',
        'given_time',
        'date_time',
        'amount_received',
    )
    search_fields = [
        'artwork',
        'collaborating_museum',
    ]
    list_filter = (
        'collaborating_museum',
    )

@admin.register(Restoration)
class RestorationAd(admin.ModelAdmin):
    list_display = (
        'artwork',
        'restoration_type',
        'date_time',
        'finish_date',
    )
    search_fields = [
        'artwork',
        'restoration_type',
    ]
    list_filter = (
        'restoration_type',
    )

@admin.register(Exibition)
class ExibitionAd(admin.ModelAdmin):
    list_display = (
        'artwork',
        'date_time',
    )
    search_fields = [
        'artwork',
    ]

@admin.register(Room)
class RoomAd(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = [
        'name',
    ]

