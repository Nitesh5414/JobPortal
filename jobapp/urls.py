from django.urls import path
from jobapp import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.index_page),
    path('register/', views.user_register_view),
    path('login/', auth_view.LoginView.as_view(template_name = 'jobapp/login.html')),
    path('logout/', auth_view.LogoutView.as_view()),
    path('home/', views.home_page_view),



    ################ For IT jobs #####################
    path('add_it/', views.add_it_job_view),
    path('show_it/', views.show_it_jobs_view),
    path('update_it/<int:id>', views.update_it_jobs_view),
    path('delete_it/<int:id>', views.delete_it_jobs_view),

    ############# for Mech Jobs #######################
    path('add_mech/', views.add_mech_job_view),
    path('show_mech/', views.show_mech_jobs_view),
    path('update_mech/<int:id>', views.update_mech_jobs_view),
    path('delete_mech/<int:id>', views.delete_mech_jobs_view),

    ############# for Civil Jobs #######################
    path('add_civil/', views.add_civil_job_view),
    path('show_civil/', views.show_civil_jobs_view),
    path('update_civil/<int:id>', views.update_civil_jobs_view),
    path('delete_civil/<int:id>', views.delete_civil_jobs_view),

    ############# for add images #######################
    path('add_image/', views.add_image_view),
    path('read_image/', views.read_image_view),



]
