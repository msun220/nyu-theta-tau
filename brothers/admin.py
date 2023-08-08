from django.contrib import admin
from brothers.models import Brother, PledgeClass


@admin.register(PledgeClass)
class PledgeClassAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]


@admin.register(Brother)
class BrotherAdmin(admin.ModelAdmin):
    list_display = [
        "brother_number",
        "name",
        "major",
        "eboard",
        "chair",
        "quote",
        "grad_year",
        "description",
        "pledge_class",
        "active"
    ]
