from django.shortcuts import render,  get_object_or_404
from django.views.decorators.http import require_POST
from Inventory.models import Donut

@require_POST
def post_shopping(request, donut_id):
    donut = get_object_or_404(Donut, id=donut_id)
    