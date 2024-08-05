from django.urls import path
from .import views

urlpatterns = [
    path("",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    path("dashboard/",views.dashboardView,name="dashboardView"),
    path("assignbooks/",views.assignBookView,name="assignBookView"),
    path("requestbooks/",views.requestBookView,name="requestBookView"),
    path("approvebook/<str:name>/<str:book_title>/",views.approvedRequest,name="approvedRequest"),
    path("editpage/<int:pk>",views.Editpage,name="editpage"),
    path("Update/<int:pk>",views.update_view,name="update"),
    path("delete/<int:pk>",views.DeleteData,name="delete"),  
]