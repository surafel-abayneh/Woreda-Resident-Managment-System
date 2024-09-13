""" from django.contrib import admin
from .models import PersonalInformation,IDCard

@admin.register(PersonalInformation)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('F_Name', 'M_Name', 'L_Name', 'sex', 'dob', 'place_of_birth', 'Nationality', 'phone_number')
    search_fields = ('first_name', 'last_name', 'place_of_birth', 'Nationality', 'phone_number')
    list_filter = ('sex', 'nationality', )
    ordering = ('last_name',)
    fieldsets = (
        (None, {
            'fields': ('F_Name', 'M_Name', 'L_Name', 'sex', 'dob', 'place_of_birth', 'Nationality', 'phone_number', 'photograph')
        }),
        
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

@admin.register(IDCard)
class IdinfoAdmin(admin.ModelAdmin):
    list_display = ('id_number', 'get_first_name', 'get_middle_name', 'get_last_name', 'get_dob', 'get_sex', 'get_phone_number', 'house_number', 'given_date', 'expiration_date', 'emergency_number')
    search_fields = ('id_number', 'personal_info__first_name', 'personal_info__last_name', 'emergency_number', 'emergency_contact_name')
    list_filter = ('personal_info__sex', 'given_date', 'expiration_date')

    def get_first_name(self, obj):
        return obj.first_name

    def get_middle_name(self, obj):
        return obj.middle_name

    def get_last_name(self, obj):
        return obj.last_name

    def get_dob(self, obj):
        return obj.dob

    def get_sex(self, obj):
        return obj.sex

    def get_phone_number(self, obj):
        return obj.phone_number

    get_first_name.short_description = 'First Name'
    get_middle_name.short_description = 'Middle Name'
    get_last_name.short_description = 'Last Name'
    get_dob.short_description = 'Date of Birth'
    get_sex.short_description = 'Sex'
    get_phone_number.short_description = 'Phone Number'
 """