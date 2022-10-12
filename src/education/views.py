from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from education import models,forms

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
        term_ids = request.POST.getlist('TermId')
        education_contents = request.POST.getlist('education_content')
        session_numbers = request.POST.getlist('session_number')
        max_students = request.POST.getlist('max_student')
        session_prices = request.POST.getlist('session_price')
        nsession_prices = request.POST.getlist('nsession_price')

        if form.is_valid():
            obj = form.save()
            obj.user = request.user
            obj.save()
            if len(term_ids) > 0:
                for term_id,education_content,session_number,max_student,session_price,nsession_price in zip(term_ids,education_contents,session_numbers,max_students,session_prices,nsession_prices):
                    models.EnglishInstituteForm.objects.create(english_institute_register = obj , english_institute_define_term = models.EnglishInstituteDefineTerm.objects.get(id = term_id ),education_content = education_content, session_number = session_number,max_student = max_student, session_price = session_price,nsession_price = nsession_price )
            return HttpResponseRedirect(reverse('education:froms_list'))

    return render(request, 'education/english_institude_register.html', context)


def forms_list(request):
   english_institutes_registers = models.EnglishInstituteRegister.objects.filter(user=request.user)

   context = {
    'english_institutes_registers' : english_institutes_registers
   }

   return render(request, 'education/forms_list.html', context)
        
