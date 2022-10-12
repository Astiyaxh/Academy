from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from education import models,forms
from django.urls import reverse

@login_required
def english_institude_register(request):
    form = forms.EnglishInstituteRegisterForm(request.POST or None)
    institutes_english = models.EnglishInstitute.objects.filter(status = 1)
    cities = models.City.objects.filter(status = 1)
    districts = models.District.objects.filter(status = 1)
    areas = models.Area.objects.filter(status = 1)
    terms = models.EnglishInstituteDefineTerm.objects.filter(status = 1)
    context = dict()
    context.update({
        'form': form,
        'institutes_english':institutes_english,
        'cities':cities,
        'districts':districts,
        'areas':areas,
        'terms':terms,
    })


    if request.method == "POST":
        institue_english = request.POST.get('institue_english')
        city = request.POST.get('city')
        district = request.POST.get('district')
        area = request.POST.get('area')

        if form.is_valid():
            obj = form.save()
            obj.update(institue_english = institue_english, city = city, district = district, area = area  )


    return render(request, 'education/english_institude_register.html', context)


def english_institute_forms_list(request):
   english_institutes_registers = models.EnglishInstituteRegister.objects.filter(user=request.user)
   context = {
    'english_institutes_registers' : english_institutes_registers
   }
   return render(request, 'education/forms_list.html', context)


def delete_english_institute_forms_list(request,id):
    obj = get_object_or_404(models.EnglishInstituteRegister, id = id)
    try:
        obj.delete()
    except:
        obj.status = -1
        obj.save()

    return HttpResponseRedirect(reverse("education:english_institute_forms_list"))
 

        
