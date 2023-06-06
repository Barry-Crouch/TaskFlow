from django.shortcuts import render
from django.views import View


class ProjectView(View):
    def get(self, request):
        
        return render(request, 'project/project_view.html')