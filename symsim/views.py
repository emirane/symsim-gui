from django.shortcuts import render
from symsim.forms import LoginForm, RegistrationForm, Model_name_form
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib import auth
from symsim.models import Simulation_report, User_model, Computing_node, Data_generator, Disk_server, Switch
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


def base_view(request):
    return render(request, 'base.html')


def example_nica_view(request):
    return render(request, 'example_nica.html')


def example_cas_view(request):
    return render(request, 'example_cas.html')


def account_view(request):
    if request.user.is_authenticated:
        return render(request, 'account.html')
    else:
        return render(request, 'base.html')


def project_view(request):
    return render(request, 'project.html')


def usage_view(request):
    return render(request, 'usage.html')


def technology_view(request):
    return render(request, 'technology.html')


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('base'))
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


def registration_view(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        first_name = form.cleaned_data['first_name']
        new_user.username = username
        new_user.set_password(password)
        new_user.first_name = first_name
        new_user.email = email
        new_user.save()
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('base'))
    context = {
        'form': form,
    }
    return render(request, 'registration.html', context)


def create_model_name(request):
    form = Model_name_form(request.POST or None)
    if form.is_valid():
        model_name = form.cleaned_data['model_name']
        new_model = User_model.objects.create(
            user=request.user,
            model_name=model_name
        )
        new_model.save()
        model_id = new_model.id
        return HttpResponseRedirect(reverse('create_model', kwargs={'id': model_id}))
    else:
        context = {
            'form': form,
        }
        return render(request, 'create_model_name.html', context)


def create_model(request, id):

    user_model = User_model.objects.get(id=id)
    content = {"user_model": user_model}

    return render(request, 'create_model.html', content)


def get_user_model(request):
    user_model = User_model.objects.filter(user=request.user)
    content = {"user_model": user_model}

    return render(request, 'account.html', content)


def get_model_device(request):
    user_model = User_model.objects.filter(user=request.user)
    content = {"user_model": user_model}

    return render(request, 'account.html', content)


@csrf_exempt
def create_comp_node(request):
    if request.method == "POST":
        cn_name = request.POST["cn_name"]
        model_name = request.POST["model_name"]
        ncpu = request.POST["ncpu"]
        cpu_speed = request.POST["cpu_speed"]
        avr_data_value = request.POST["avr_data_value"]
        model_id = User_model.objects.get(model_name=model_name).id
        attribute = {"cn_name": cn_name, "ncpu": ncpu, "cpu_speed": cpu_speed, "avr_data_value": avr_data_value,
                     "model_id": model_id}
        obj, created = Computing_node.objects.update_or_create(cn_name=cn_name, model_id=model_id, defaults=attribute)

        if created:
            return HttpResponse("Object create!")
        else:
            return HttpResponse("Object update!")
    else:
        return HttpResponse("Error!")


@csrf_exempt
def create_data_generator(request):
    if request.method == "POST":
        dg_name = request.POST["dg_name"]
        model_name = request.POST["model_name"]
        freq_data = request.POST["freq_data"]
        data_value = request.POST["data_value"]
        model_id = User_model.objects.get(model_name=model_name).id
        attribute = {"dg_name": dg_name, "freq_data": freq_data, "data_value": data_value, "model_id": model_id}
        obj, created = Data_generator.objects.update_or_create(dg_name=dg_name, model_id=model_id, defaults=attribute)

        if created:
            return HttpResponse("Object create!")
        else:
            return HttpResponse("Object update!")
    else:
        return HttpResponse("Error!")


@csrf_exempt
def create_disk_server(request):
    if request.method == "POST":
        disk_server_name = request.POST["disk_server_name"]
        model_name = request.POST["model_name"]
        disk_pool_size = request.POST["disk_pool_size"]

        model_id = User_model.objects.get(model_name=model_name).id
        attribute = {"disk_server_name": disk_server_name, "disk_pool_size": disk_pool_size, "model_id": model_id}
        obj, created = Disk_server.objects.update_or_create(disk_server_name=disk_server_name, model_id=model_id, defaults=attribute)

        if created:
            return HttpResponse("Object create!")
        else:
            return HttpResponse("Object update!")
    else:
        return HttpResponse("Error!")


@csrf_exempt
def create_switch(request):
    if request.method == "POST":
        switch_name = request.POST["switch_name"]
        model_name = request.POST["model_name"]
        sw_capacity = request.POST["sw_capacity"]

        model_id = User_model.objects.get(model_name=model_name).id
        attribute = {"switch_name": switch_name, "sw_capacity": sw_capacity, "model_id": model_id}
        obj, created = Switch.objects.update_or_create(switch_name=switch_name, model_id=model_id, defaults=attribute)

        if created:
            return HttpResponse("Object create!")
        else:
            return HttpResponse("Object update!")
    else:
        return HttpResponse("Error!")


def get_simulation_report(request):
    return render(request, 'graphics.html')


@csrf_exempt
def ajax_graph(request):
    if request.method == "POST":
        sw0 = request.POST["sw0"]
        sw1 = request.POST["sw1"]
        sw2 = request.POST["sw2"]
        sw3 = request.POST["sw3"]
        dc_core = request.POST["dc_core"]
        operation = request.POST["operation"]
        simid = request.POST["simid"]
        simulation_report = Simulation_report.objects.filter(operation=operation, simulation_id=simid,
                                                             int1=sw0, system_time__lte='30000').values_list('system_time', 'double1').order_by('system_time')
        simulation_report2 = Simulation_report.objects.filter(operation=operation, simulation_id=simid,
                                                             int1=sw1).values_list('double1').order_by('system_time')
        simulation_report3 = Simulation_report.objects.filter(operation=operation, simulation_id=simid,
                                                             int1=sw2).values_list('double1').order_by('system_time')
        simulation_report4 = Simulation_report.objects.filter(operation=operation, simulation_id=simid,
                                                              int1=sw3).values_list('double1').order_by('system_time')
        simulation_report5 = Simulation_report.objects.filter(operation=operation, simulation_id=simid,
                                                              int1=dc_core).values_list('double1').order_by('system_time')

        return JsonResponse({'sim_rep1': list(simulation_report),
                             'sim_rep2': list(simulation_report2),
                             'sim_rep3': list(simulation_report3),
                             'sim_rep4': list(simulation_report4),
                             'sim_rep5': list(simulation_report5)
        })
    else:
        return HttpResponse("Ошибка")


@csrf_exempt
def ajax_graph2(request):
    if request.method == "POST":
        simulation_report = Simulation_report.objects.filter(operation='37', simulation_id='2',
                                                             object='8', event='3', int1='36').values_list('system_time', 'double1')
        simulation_report2 = Simulation_report.objects.filter(operation='37', simulation_id='2',
                                                             object='8', event='3', int1='24').values_list('double1')
        return JsonResponse({'sim_rep': list(simulation_report),
                             'sim_rep2': list(simulation_report2)})
    else:
        return HttpResponse("Error!")
