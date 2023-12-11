from django.contrib import admin
from .models import Category, Event


# Registering the Category model with the Django admin interface.
admin.site.register(Category)

# Registering the Event model with the Django admin interface.
admin.site.register(Event)
