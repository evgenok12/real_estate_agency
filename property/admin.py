from django.contrib import admin
from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Flat.owner_set.through
    raw_id_fields = ('owner', )


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('id', 'owner', 'town', 'address')
    readonly_fields = ('created_at', )
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town', 'owner_pure_phone', 'owners_phonenumber')
    list_editable = ('new_building', )
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by', )
    inlines = (OwnerInline, )


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')


class OwnerAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name', 'pure_phone')
    list_display = ('id', 'name', 'pure_phone')
    raw_id_fields = ('flats', )


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
