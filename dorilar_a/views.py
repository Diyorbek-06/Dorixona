from django.shortcuts import render
from django.views import View
from .models import Dori
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from .forms import DoriForm

# Create your views here.


def home_page(request):
    return render(request, 'home.html')





class DoriList(View):
    def get(self, request):
        t = request.GET.get('t')
        dorilar = Dori.objects.filter(nomi__icontains=t) if t else Dori.objects.all()
        return render(request, 'dori_list.html', {'dorilar':dorilar})



class DoriDetail(DetailView):
    model = Dori
    template_name = 'dori_detail.html'
    context_object_name = 'dori'

class DoriDelete(DeleteView):
    model = Dori
    success_url = reverse_lazy('dori-list')
    template_name = 'dori_delete.html'
    context_object_name = 'dori'

class DoriCreate(CreateView):
    model = Dori
    form_class = DoriForm
    success_url = reverse_lazy('dori-list')
    template_name = 'dori_create.html'
    # fields = '__all__'

class DoriUpdate(UpdateView):
    model = Dori
    template_name = 'dori_update.html'
    fields = ['make', 'nomi', 'price', 'xususiyat', 'miqdori', 'tugash_muddati', 'image']

    def get_success_url(self):
        return reverse_lazy('dori-detail', kwargs={'pk': self.object.pk})

























# class SearchList(View):
#     def get(self, request):
#         t = request.GET.get('t')
#         dorilar = Dori.objects.filter(nomi__icontains=t)
#         return render(request, 'search.html', {'dorilar': dorilar})


## postgreslik ish
# class DoriList(View):
#     def get(self, request):
#         t = request.GET.get('t')
#         dorilar = Dori.objects.annotate(SearchVector('xususiyat', 'name'))(search=t) if t else Dori.objects.all()
#         return render(request, 'dori_list.html', {'dorilar':dorilar})








# def dori_list(request):
#     dorilar = Dori.objects.all()
#     context = {'dorilar' : dorilar}
#     return render(request, 'dorilar/dori_list.html', context=context)

# def dori_detail(request, pk):
#     dori = Dori.objects.get(pk=id)
#     context = {'dori':dori}
#     return render(request, 'dorilar/dori_detail.html' , context=context)

# from django.shortcuts import render, get_object_or_404

# def dori_detail(request, id):
#     dori = get_object_or_404(Dori, pk=id)
#     return render(request, 'dorilar/dori_detail.html', {'dori': dori})
