# Python imports
# Django imports
from django.contrib import admin
# Third party app imports
# Local app imports
from .models import Category


# Register your models here.
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["id", "sort", "name", "css_class", "updated", "timestamp"]
    list_display_links = ["id"]
    list_editable = ["sort", "name", "css_class"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["name"]

    class Meta:
        model = Category


admin.site.register(Category, CategoryModelAdmin)

