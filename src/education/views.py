from django.shortcuts import render,HttpResponseRedirect ,get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required,user_passes_test
from education import models,forms
from itertools import chain

@login_required
@user_passes_test(lambda u: u.groups.filter(name='English').exists())
def english_institute_register(request):
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
            return HttpResponseRedirect(reverse('education:english_institute_forms_list'))

    return render(request, 'education/english_institude_register.html', context)


@login_required
@user_passes_test(lambda u: u.groups.filter(name='English').exists())
def english_institute_edit(request,id):
    obj = get_object_or_404(models.EnglishInstituteRegister, id = id)
    form = forms.EnglishInstituteRegisterForm(request.POST or None, instance= obj )
    terms = models.EnglishInstituteDefineTerm.objects.filter(status = 1)
    context = dict()
    context.update({
        'terms':terms,
        'form':form,
    })

    if  models.EnglishInstituteForm.objects.filter(english_institute_register = obj).exists():
        table_terms = models.EnglishInstituteForm.objects.filter(english_institute_register = obj)
        context.update({
            'table_terms':table_terms,
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
            if  models.EnglishInstituteForm.objects.filter(english_institute_register = obj).exists():
                models.EnglishInstituteForm.objects.filter(english_institute_register = obj).delete()
            if len(term_ids) > 0:
                for term_id,education_content,session_number,max_student,session_price,nsession_price in zip(term_ids,education_contents,session_numbers,max_students,session_prices,nsession_prices):
                    models.EnglishInstituteForm.objects.create(english_institute_register = obj , english_institute_define_term = models.EnglishInstituteDefineTerm.objects.get(id = term_id ),education_content = education_content, session_number = session_number,max_student = max_student, session_price = session_price,nsession_price = nsession_price )
            return HttpResponseRedirect(reverse('education:english_institute_forms_list'))

    return render(request, 'education/english_institude_register.html', context)


@login_required
@user_passes_test(lambda u: u.groups.filter(name='NonProfit').exists())
def none_profit_form_register(request):
    form = forms.NoneProfitFormForm(request.POST or None)
    terms = models.NonProfitInstituteDefineTerm.objects.filter(status = 1)
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
        max_hours = request.POST.getlist('max_hour')
        tuitions = request.POST.getlist('tution')

        if form.is_valid():
            obj = form.save()
            obj.user = request.user
            obj.save()
            if len(term_ids) > 0:
                for term_id,education_content,session_number,max_student,max_hour,tution in zip(term_ids,education_contents,session_numbers,max_students,max_hours,tuitions):
                    models.NoneProfitFormTable.objects.create(none_profit_form = obj , non_profit_institute_define_term = models.NonProfitInstituteDefineTerm.objects.get(id = term_id ),education_content = education_content, session_number = session_number,max_student = max_student, max_hour = max_hour,tuition = tution )
            return HttpResponseRedirect(reverse('education:english_institute_forms_list'))

    return render(request, 'education/non_profit_institude_register.html', context)


@login_required
@user_passes_test(lambda u: u.groups.filter(name='NonProfit').exists())
def none_profit_form_edit(request,id):
    obj = get_object_or_404(models.NoneProfitForm, id = id)
    form = forms.NoneProfitFormForm(request.POST or None, instance= obj )
    terms = models.NonProfitInstituteDefineTerm.objects.filter(status = 1)
    context = dict()
    context.update({
        'terms':terms,
        'form':form,
    })

    if  models.NoneProfitFormTable.objects.filter(none_profit_form = obj).exists():
        table_terms = models.NoneProfitFormTable.objects.filter(none_profit_form = obj)
        context.update({
            'table_terms':table_terms,
        })
        
    if request.method == "POST":
        term_ids = request.POST.getlist('TermId')
        education_contents = request.POST.getlist('education_content')
        session_numbers = request.POST.getlist('session_number')
        max_students = request.POST.getlist('max_student')
        max_hours = request.POST.getlist('max_hour')
        tuitions = request.POST.getlist('tution')


        if form.is_valid():
            obj = form.save()
            obj.user = request.user
            obj.save()
            if  models.NoneProfitFormTable.objects.filter(none_profit_form = obj).exists():
                models.NoneProfitFormTable.objects.filter(none_profit_form = obj).delete()
            if len(term_ids) > 0:
                for term_id,education_content,session_number,max_student,max_hour,tution in zip(term_ids,education_contents,session_numbers,max_students,max_hours,tuitions):
                    models.NoneProfitFormTable.objects.create(none_profit_form = obj , non_profit_institute_define_term = models.NonProfitInstituteDefineTerm.objects.get(id = term_id ),education_content = education_content, session_number = session_number,max_student = max_student, max_hour = max_hour,tuition = tution )
            return HttpResponseRedirect(reverse('education:english_institute_forms_list'))

    return render(request, 'education/non_profit_institude_register.html', context)


@login_required
def english_institute_forms_list(request):
   english_institutes_registers = models.EnglishInstituteRegister.objects.filter(user=request.user)
   non_profit_forms = models.NoneProfitForm.objects.filter(user=request.user)
   query_set = chain(english_institutes_registers, non_profit_forms)

   context = {
    'english_institutes_registers' : query_set
   }
   return render(request, 'education/forms_list.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='English').exists())
def delete_english_institute_forms_list(request,id):
    obj = get_object_or_404(models.EnglishInstituteRegister, id = id)
    try:
        obj.delete()
    except:
        obj.status = -1
        obj.save()

    return HttpResponseRedirect(reverse("education:english_institute_forms_list"))

@login_required
@user_passes_test(lambda u: u.groups.filter(name='English').exists())
def send_english_institute_forms_list(request,id):
    obj = get_object_or_404(models.EnglishInstituteRegister, id = id)
    obj.send_status = 2
    obj.save()

    return HttpResponseRedirect(reverse("education:english_institute_forms_list"))



# Admin views for EnglishInstituteRegister

@login_required
@user_passes_test(lambda u: u.groups.filter(name='SuperVisor').exists())
def admin_forms_list(request):
   english_institutes_registers = models.EnglishInstituteRegister.objects.filter(send_status=2)
   nonprofit_form = models.NoneProfitForm.objects.filter(send_status=2)
   query_sets = chain(english_institutes_registers, nonprofit_form)
   context = {
    'query_sets' : query_sets
   }
   return render(request, 'education/admin_forms_list.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name='SuperVisor').exists())
def admin_rejected_forms_list(request,id):
    obj = get_object_or_404(models.EnglishInstituteRegister, id = id)
    obj.send_status = 3
    obj.save()

    return HttpResponseRedirect(reverse("education:admin_forms_list"))



@login_required
@user_passes_test(lambda u: u.groups.filter(name='SuperVisor').exists())
def admin_accepted_forms_list(request,id):
    obj = get_object_or_404(models.EnglishInstituteRegister, id = id)
    obj.send_status = 4
    obj.save()

    return HttpResponseRedirect(reverse("education:admin_forms_list"))



#  Nonprofit institute 

@login_required
def delete_nonprofit_institute_forms_list(request, id):
    obj = get_object_or_404(models.NoneProfitForm, id = id)
    try:
        obj.delete()
    except:
        obj.status = -1
        obj.save()

    return HttpResponseRedirect(reverse("education:english_institute_forms_list"))

@login_required
def send_nonprofit_institute_forms_list(request, id):
    obj = get_object_or_404(models.NoneProfitForm, id = id)
    obj.send_status = 2
    obj.save()

    return HttpResponseRedirect(reverse("education:english_institute_forms_list"))



# Admin views for nonprofit institute

@login_required
def admin_nonprofit_institute_rejected_forms_list(request, id):
    obj = get_object_or_404(models.NoneProfitForm, id = id)
    obj.send_status = 3
    obj.save()

    return HttpResponseRedirect(reverse("education:admin_forms_list"))


@login_required
def admin_nonprofit_institute_accepted_forms_list(request, id):
    obj = get_object_or_404(models.NoneProfitForm, id = id)
    obj.send_status = 4
    obj.save()

    return HttpResponseRedirect(reverse("education:admin_forms_list"))
