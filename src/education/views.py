from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from education import models,forms
from django.urls import reverse

@login_required
def english_institude_register(request):
    form = forms.EnglishInstituteRegisterForm(request.POST or None)
    terms = models.EnglishInstituteDefineTerm.objects.filter(status = 1)
    context = dict()
    context.update({
        'terms':terms,
        'form':form,
    })

    if request.method == "POST":
        if form.is_valid():
            obj = form.save()
            obj.user = request.user
            obj.save()

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
