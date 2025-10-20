from django.contrib import admin
from .models import Form, Address

@admin.action(description="Mark selected as active")
def mark_as_active(modeladmin, request, queryset):
    queryset.update(is_active=True)

class AddressInline(admin.TabularInline):
    model = Address
    extra = 1

class FormAdmin(admin.ModelAdmin):
   fieldsets = (
       ("Personal Information", {
            "fields": ("first_name", "last_name", "email")
        }),
        ("Job Details", {
            "fields": ("occupation", "date"),
            "classes": ("collapse",),  # collapsible section
        }),
   )

   inlines = [AddressInline]

   list_display = ("first_name", "last_name", "email", "occupation", "date")
   list_display_links = ("first_name", "last_name");  # Which fields link to the edit page
   search_fields = ("first_name", "last_name", "email");
   list_filter = ("date", "occupation");
   ordering = ("first_name",);
   readonly_fields = ("occupation",);
   list_editable = ("occupation",);
   list_per_page = 20;


   actions = [mark_as_active]

admin.site.register(Form, FormAdmin);
