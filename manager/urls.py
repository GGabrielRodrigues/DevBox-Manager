from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='manager/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    path('projeto/novo/', views.project_create, name='project_create'),
    path('projeto/<int:pk>/', views.project_detail, name='project_detail'),
    path('projeto/<int:pk>/editar/', views.project_edit, name='project_edit'),
    path('projeto/<int:pk>/excluir/', views.project_delete, name='project_delete'),
    
    path('projeto/<int:project_pk>/caixinha/nova/', views.contentbox_create, name='contentbox_create'),
    path('caixinha/<int:pk>/', views.contentbox_detail, name='contentbox_detail'),
    path('caixinha/<int:pk>/editar/', views.contentbox_edit, name='contentbox_edit'),
    path('caixinha/<int:pk>/excluir/', views.contentbox_delete, name='contentbox_delete'),
    
    path('relatorio/', views.report_view, name='report'),
]
