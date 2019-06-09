from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView
from .models import News_table

def main_page(task):
    news_dict={'news':News_table.objects.all()}
    return render(task, 'blog/main_page.html', news_dict)

class NewsList(ListView):
    model = News_table
    template_name = 'blog/main_page.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'news'
    ordering = ['-date_posted']

class NewsCreate(LoginRequiredMixin, CreateView):
    model = News_table
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
		
def descriptive_page(task):
    return render(task, 'blog/descriptive_page.html', {'title':'About'})
