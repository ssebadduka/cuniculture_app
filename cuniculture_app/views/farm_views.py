from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from cuniculture_app.forms.farm_forms import FarmForm
from cuniculture_app.selectors.farms_selectors import get_farms, get_farm

def manage_farms(request):

    farms = get_farms()
    farm_form = FarmForm()

    if request.method == "POST":
        farm_form = FarmForm(request.POST, request.FILES)

        if farm_form.is_valid():
            farm_form.save()
            messages.success(request, 'Farm Record saved Successfully!')
        else:
            messages.warning(request, 'Operation Not Successfull')
        
        return HttpResponseRedirect(reverse(manage_farms))

    context = {
        "farm": "active",
        "farms": farms,
        "farm_form":farm_form
    }
    return render (request, "farms/manage_farms.html", context)

def edit_farm_view(request, farm_id):

    farm = get_farm(farm_id)
    farm_form = FarmForm(instance=farm)

    if request.method == "POST":
        farm_form = FarmForm(request.POST, request.FILES)

        if farm_form.is_valid():
            farm_form.save()
            messages.success(request, 'Changes saved Successfully!')
        else:
            messages.warning(request, 'Operation Not Successfull')
        
        return HttpResponseRedirect(reverse(manage_farms))

def delete_farm_view(request, farm_id):
    farm = get_farm(farm_id)

    farm.delete()
    messages.success(request, 'Farm Deleted Successfull')
        
    return HttpResponseRedirect(reverse(manage_farms))
