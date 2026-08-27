from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .forms import PostagemForm
from .models import PostagemModel

def home_view(request):
    context = {
        "posts":PostagemModel.objects.all()
    }
    return render(request, 'home.html', context)

def form_view(request:HttpRequest):

    if request.method == "POST":
        form_inst = PostagemForm(request.POST)
        if form_inst.is_valid():
            form_inst.save()
            return redirect("home")

    else:
        form_inst = PostagemForm()

    context = {"form": form_inst}
    return render(request, 'form.html', context)

def post_delete(request:HttpRequest, id):
    post_inst = get_object_or_404(PostagemModel, id=id)
    post_inst.delete()
    return redirect("home")

def post_edit(request:HttpRequest, id):
    post_inst = get_object_or_404(PostagemModel, id=id)
    if request.method == "POST":
        form_inst = PostagemForm(request.POST, instance=post_inst)
        if form_inst.is_valid():
            form_inst.save()
            return redirect('home')

    form_inst = PostagemForm(instance=post_inst)
    context = {'form':form_inst}
    return render(request, 'edit.html', context)
