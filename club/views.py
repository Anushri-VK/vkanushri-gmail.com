from django.shortcuts import render,redirect
from club.models import Complete


# Create your views here.
# def home_page(request):

# 			trending_posts=home_page.objects.all()
# 			events=home_page.objects.all()
# 			coupons=home_page.objects.all()
# 			category=home_page.objects.all()
# 			most_popular=home_page.objects.all()

# 			return redirect("/home/")
# 		return render(request,"home.html")


def home(request):
	all=Complete.objects.all()
	return render(request,"home.html",{"item":all})

def coupons(request):
	all_1=Complete.objects.all()
	return render(request,"coupons.html",{"item":all_1})

def events(request):
	all_2=Complete.objects.all()
	return render(request,"events.html",{"item":all_2})

def blogs(request):
	all_3=Complete.objects.all()
	return render(request,"blogs.html",{"item":all_3})

def blog_articles(request):
	all_4=Complete.objects.all()
	return render(request,"blog_article.html",{"item":all_4})

def blog_articles_1(request):
	all_5=Complete.objects.all()
	return render(request,"blog_articles_1.html",{"item":all_5})