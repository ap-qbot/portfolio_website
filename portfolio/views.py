from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Prefetch
from .models import Project, Category


class PortfolioView(ListView):
    model = Project
    template_name = 'portfolio/home.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['active_category'] = self.request.GET.get('category', 'all')
        return context

    def get_queryset(self):
        category = self.request.GET.get('category')
        # Use select_related to optimize database queries
        queryset = Project.objects.select_related('category')

        if category and category != 'all':
            return queryset.filter(category__slug=category)
        return queryset.all()  # Will use the ordering from Meta class

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'