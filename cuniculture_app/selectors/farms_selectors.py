from cuniculture_app.models.farms import Farm

def get_farms():
    return Farm.objects.all()

def get_farm(farm_id):
    return Farm.objects.get(pk=farm_id)