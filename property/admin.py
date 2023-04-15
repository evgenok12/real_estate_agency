from django.contrib import admin
from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ('owner', )


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('id', 'town', 'address')
    readonly_fields = ('created_at', )
    list_display = ('id', 'town', 'address', 'price', 'new_building', 'construction_year')
    list_editable = ('new_building', )
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by', )
    inlines = (OwnerInline, )


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name', 'pure_phone')
    list_display = ('id', 'name', 'pure_phone')
    raw_id_fields = ('flats', )

