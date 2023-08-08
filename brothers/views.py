import json
from django.http import JsonResponse
from .models import Brother, PledgeClass
from .json import ModelEncoder
from django.views.decorators.http import require_http_methods


class PledgeClassEncoder(ModelEncoder):
    model = PledgeClass
    properties = [
        "name"
    ]


class BrotherEncoder(ModelEncoder):
    model = Brother
    properties = [
        "brother_number",
        "name",
        "major",
        "eboard",
        "chair",
        "quote",
        "grad_year",
        "description",
        "active",
        "headshot",
        "pledge_class"
    ]

    encoders = {
        "pledge_class": PledgeClassEncoder()
    }


@require_http_methods(["GET"])
def list_actives(request):

    if request.method == "GET":
        actives = {}
        brothers = Brother.objects.filter(active=True).order_by('brother_number')
        for brother in brothers:
            pledge_class = brother.pledge_class.name
            if pledge_class not in actives:
                actives[pledge_class] = []
            actives[pledge_class].append(brother)

        return JsonResponse(
            {'actives': actives},
            encoder=BrotherEncoder,
            safe=False
        )


@require_http_methods(["GET"])
def list_inactives(request):

    if request.method == "GET":
        inactives = {}
        brothers = Brother.objects.filter(active=False).order_by('brother_number')
        for brother in brothers:
            pledge_class = brother.pledge_class.name
            if pledge_class not in inactives:
                inactives[pledge_class] = []
            inactives[pledge_class].append(brother)

        return JsonResponse(
            {'inactives': inactives},
            encoder=BrotherEncoder,
            safe=False
        )


@require_http_methods(["GET"])
def list_eboard(request):

    if request.method == "GET":
        eboard_map = {
            "Regent": None,
            "Vice Regent": None,
            "Recording Secretary": None,
            "Treasurer": None,
            "Corresponding Secretary": None
            }
        eboard = Brother.objects.filter(eboard=True)
        for eboard_member in eboard:
            if eboard_member.chair in eboard_map:
                eboard_map[eboard_member.chair] = eboard_member

        return JsonResponse(
            {'eboard_map': eboard_map},
            encoder=BrotherEncoder,
            safe=False
        )
