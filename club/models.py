from django.db import models

CHOICE = (
	("trending_posts","LATEST_POSTS"),
	("events","EVENTS"),
	("coupons","COUPONS"),
	("category","CATEGORY"),
	("most_popular","MOST_POPULAR"),
	("blogs","BLOGS"),
	("blog_articles","BLOG_ARTICLES"),
	("blog_articles_1","BLOG_ARTICLES_1"),
	# ("explore","EXPLORE"),
)

class Complete(models.Model):
	title=models.CharField(max_length=100,null=True,blank=True)
	image_url=models.TextField(null=True,blank=True)
	description=models.TextField()
	card_type=models.CharField(choices=CHOICE,default="trending_posts",max_length=100)
	organized_by=models.CharField(max_length=100,null=True,blank=True)
	timestamp=models.DateTimeField(auto_now=True)
	# end_date=models.DateTimeField(auto_now=True)
	venue=models.CharField(max_length=100,null=True,blank=True)
	price=models.CharField(max_length=100,null=True,blank=True)
	# date=models.CharField(max_length=100,null=True,blank=True)


	def __str__(self):
		return f"{self.title} | {self.description} | {self.image_url} | {self.card_type} "




