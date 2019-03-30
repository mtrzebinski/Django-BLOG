from django.shortcuts import render
from .models import News_table

def main_page(task):
    news_dict={'news':News_table.objects.all()}
    return render(task, 'blog/main_page.html', news_dict)

def descriptive_page(task):
    return render(task, 'blog/descriptive_page.html', {'title':'About'})
