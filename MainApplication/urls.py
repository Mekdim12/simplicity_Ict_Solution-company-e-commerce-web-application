
from django.contrib import admin
from django.urls import path
from django.urls import path,include
from . import views



urlpatterns = [
    path('', views.HomePage, name='main'),
    path('public/aboutus',views.PublicAboutUs , name ='PublicAboutUs'),
    path('public/contactus', views.PublicContactUs, name ='PublicContactUs'),
    path('login/', views.Login, name ='login'),
    path('signup', views.SignUp, name = 'signup'),
    path('public/dashboard',views.dashBoard, name="dashboard"),
    
    path('public/shop',views.Shop, name="shop"),
    path('public/cart/',views.Cart, name="cart"),
    path('public/nocart',views.NoCart, name="nocart"),
    path('private/staff/dashboardstaff',views.DashBoardStaff, name="dashboardstaff"),
    path('private/staff/purchasingitems/<str:timestamp>',views.PurchasingItems, name="purchasingitems"),
    path('private/staff/productandservice',views.productAndService, name="productandservice"),
    path('private/staff/FormForProducts/<str:timestamp>', views.FormForProducts, name="formforproducts"),
    path('private/staff/FormServices/<str:timestamp>', views.FormForServices, name="formservices"),
    path('private/staff/FormPageContent/<str:timestamp>', views.FormPageContent, name="formpagecontent"),
    path('private/staff/deleteitemserv/<str:timestampid>', views.DeleteItem, name="deleteitem"),
    path('private/staff/deleteitemprod/<str:timestampid>', views.DeleteProd, name="deleteprod"),
    path('private/staff/DeleteConfirmationPageForPageContent/<str:timestampid>', views.DeletePageConent, name="deletepagecont"),
    path('private/staff/dashboardstaff/viewDetail/<str:timestampid>', views.ViewFullInfn, name="viewfullinfn"),
    path('private/staff/dashboardstaff/DeleteConfirmationPagePeoplesFeedBack/<str:timestampid>', views.DeleteFeedback, name="deletefeedback"),
    path('public/shop/CartChanged/<str:timestampid>',views.AddToCartButtonOperation, name="addToCart"),
    path('public/cart/DeleteConfirmationPageForCartItems/<str:timestampid>', views.DeleteCartItems, name="deletecartitems"),
    path('private/staff/purchasingitems/CustomerDetailInfnShowingPage/<str:timestampid>',views.PurchasingItemsCustViewPage, name="purchasingitemsinfnViewer"),
    path('public/dashboard/saveItemRating/<str:timestampid>',views.SaveItemRating, name="saveitemrating"),


]