from django.contrib import admin
from .models import *
from datetime import date, timedelta
from django.db.models import Sum


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
    
    current_state:Exhibition = Exhibition.objects.filter(state_ptr=states.id)
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

@admin.register(Exhibition)
class ExhibitionAd(admin.ModelAdmin):
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


@admin.action(description='Finish Restoration')
def finish_restoration(modeladmin, request, queryset):
    for a in queryset:
        a.finish_date = date.today()
        a.save()
        new = Exhibition(artwork=a.artwork, date_time=datetime.today())
        new.save()

@admin.register(CurrentRestoration)
class CurrentRestorationAd(admin.ModelAdmin):
    list_display = (
        'artwork',
        'restoration_type',
        'date_time',
        'finish_date',
    )
    actions = [finish_restoration]

    def get_queryset(self, request):
        states =[]
        for art in  Artwork.objects.all():
            if str(current_state(art)) == 'Restoration' and current_state(art).finish_date == None:
                states.append(current_state(art).id)
        qs = super().get_queryset(request).filter(pk__in=states)
        return qs

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return True

@admin.action(description='Send to Restoration')
def send_to_restoration(modeladmin, request, queryset):
    for a in queryset:
        new = Restoration(artwork=a, date_time=datetime.today())
        new.save()

@admin.register(ToRestoration)
class ToRestorationAd(admin.ModelAdmin):
    list_display = (
        'name',
        'room',
    )
    actions = [send_to_restoration]

    def get_queryset(self, request):
        restoration_state= []
        exhibition_state= []
        to_restoration=[]

        for a in Artwork.objects.all():
            currently_restoration = False
            states = Restoration.objects.filter(artwork__id=a.id).order_by('date_time')

            for b in states:
                if b.finish_date == None:
                    currently_restoration = True

            if not currently_restoration:
                if len(states) > 0:
                    restoration_state.append(states[0])
                else:
                    exhibition_state.append(a)

        for a in exhibition_state:
            states = Exhibition.objects.filter(artwork__id=a.id).order_by('date_time')
            if len(states) > 0:
                restoration_state.append(states[0])

        for a in restoration_state:
            if str(a) == 'Restoration':
                if a.finish_date != None and a.finish_date + timedelta(days=1825) <= date.today():
                    to_restoration.append(a.artwork.id)
            else:
                if a.date_time != None and a.date_time.date() + timedelta(days=1825) <= date.today():
                    to_restoration.append(a.artwork.id)

        return Artwork.objects.all().filter(id__in=to_restoration)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False