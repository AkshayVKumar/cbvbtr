"""CBV_DEMO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample/',views.sample,name="sampleFBV"),
    path('samplecbv/',views.SampleView.as_view(),name="sampleCBV"),
    path('sample1cbv/',views.Sample1View.as_view(),name="sample1CBV"),
    path('sample2cbv/',views.Sample2View.as_view(),name="sample2CBV"),
    path('templatecbv/',views.Template_View.as_view(),name="TemplateCBV"),
    path('templatecbv1/',views.Template_DemoView.as_view(),name="TemplateCBV1"),
    path('schools/',views.School_ListView.as_view(),name="school_list"),
    path('students/',views.Student_ListView.as_view(),name="Student_list"),
    path('school/<int:pk>',views.School_DetailView.as_view(),name="detail_view"),
    path('school/create/',views.Create_School.as_view(),name="create_School"),
    path('school/update/<int:pk>',views.Update_School.as_view(),name="update_school"),
    path('school/delete/<int:pk>',views.Delete_School.as_view(),name="delete_school"),
      

 ]
