from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)
	name = models.CharField(max_length=200, null=True)
	PhoneNumber = models.CharField(max_length=15,null=True,blank=True)
	email = models.EmailField(max_length=200, null=True)
	profile_pic = models.ImageField(upload_to='media',null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True,null=True)


	def __str__(self):
		return self.name

	@property
	def profile_picURL(self):
		try:
			url = self.profile_pic.url
		except:
			url = ''
		return url

class Category(models.Model):
	name = models.CharField(max_length=200 ,blank=True, null=True)

	class Meta:
		ordering = ('-name',)

	def __str__(self):
		return self.name


class Product(models.Model):
	
	STATUS =(
		('sale','SALE'),
		('new','NEW'),
		('off stock','OFF STOCK'),
		)
	PACKAGE = (

		('carton', 'Carton'),
		('6pcs', '6Pcs'),
		('1pcs', '1Pcs'),
		)

	name = models.CharField(max_length=254,blank=True, null=True)
	toto = models.IntegerField(blank=True, null=True)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, default=True,blank=True, null=True)
	prev_price = models.DecimalField(max_digits=65, decimal_places=2)
	price = models.DecimalField(max_digits=65, decimal_places=2)
	alcaholic = models.FloatField(default=0, blank=True, null=True)
	liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')
	package = models.CharField(max_length=100, choices=PACKAGE, default='carton', blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	manufacturer = models.TextField(blank=True, null=True)
	created = models.DateField(auto_now_add=True, blank=True, null=True)
	updated = models.DateField(auto_now_add=True, blank=True, null=True)
	image = models.ImageField(upload_to='media/products/' ,null=True, blank=True)
	digital = models.BooleanField(default=False, null=True, blank=True)
	status = models.CharField(max_length=256, choices=STATUS, default='sale')


	class Meta:
		ordering =('name',)
	

	def __str__(self):
		return self.name

	@property
	def num_likes(self):
		return self.liked.all().count()

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	
class Like(models.Model):

	LIKE_CHOICES = (

		('Like','Like'),
		('Unlike','Unlike'),

		)

	user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
	value = models.CharField(max_length=10, default='like', choices=LIKE_CHOICES)

	def __str__(self):
		return str(self.product)


class Order(models.Model):
	STATUS = (
		('pending','PENDING'),
		('out for delivery','OUT FOR DELIVERY'),
		('delivered','DELIVERED'),
		)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=30, blank=True, null=True, choices=STATUS, default='pending')
	complete = models.BooleanField(default=False, null=True)
	transactions_id = models.CharField(max_length=200, null=True)

	def __str__(self):
		return str(self.id)

	class meta:
		ordering=('-date_ordered')

	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital ==False:
				shipping = True
		return shipping
	

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total


class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
	order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.product.name

	class meta:
		ordering =('date_added')

	@property
	def get_total(self):
		total = self.product.price *self.quantity
		return total

class ShippingAddress(models.Model):
	customer =models.ForeignKey(Customer,on_delete=models.SET_NULL, blank=True, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
	address = models.CharField(max_length=200,null=True)
	city = models.CharField(max_length=200,null=True)
	state = models.CharField(max_length=200,null=True)
	phone = models.CharField(max_length=200,null=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address

	class Meta:
		ordering =('-date_added',)


class Regionz(models.Model):
	rname = models.CharField(max_length=254, unique=True ,blank=True, null=True)
	
	date_added  = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.rname


class Town(models.Model):
	region = models.ForeignKey(Regionz, on_delete=models.CASCADE, default=True,blank=True, null=True)
	district   = models.CharField(max_length=255, blank=True, null=True)
	county   = models.CharField(max_length=255, blank=True, null=True)
	town_name   = models.CharField(max_length=255, blank=True, null=True)
	address     = models.CharField(max_length=255,blank=True, unique=True, null=True)
	date_added  = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.town_name

