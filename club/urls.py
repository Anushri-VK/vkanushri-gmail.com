from django.urls import path
from club.views import home,coupons,events,blogs,blog_articles,blog_articles_1

urlpatterns = [
	path("home/",home),
	path("coupons/",coupons),
	path("events/",events),
	path("blogs/",blogs),
	path("blog_articles/",blog_articles),
	path("blog_articles_1/",blog_articles_1),
	# path("explore/",explore),
	# path("blogs/",blogs),
]