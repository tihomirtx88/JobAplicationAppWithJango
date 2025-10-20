from django.contrib import admin
from .models import Form

class FormAdmin(admin.ModelAdmin):
   list_display = ("first_name", "last_name", "email", "occupation", "date")
   list_display_links = ("first_name", "last_name");  # Which fields link to the edit page
   search_fields = ("first_name", "last_name", "email");
   list_filter = ("date", "occupation");
   ordering = ("first_name",);
   readonly_fields = ("occupation",);
   list_editable = ("occupation",);
   list_per_page = 20;

admin.site.register(Form, FormAdmin);
