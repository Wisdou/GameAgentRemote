from django.db import models
from django.contrib.auth.models import User


class Achievement(models.Model):
	name = models.CharField(max_length=70)
	icon = models.ImageField(upload_to="Achievements")

	class Meta:
		verbose_name = 'достижение'
		verbose_name_plural = 'достижения'

	def __str__(self):
		return self.name


class AboutUser(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	level = models.SmallIntegerField(default=0)
	exp_to_level = models.SmallIntegerField(default=0)
	money = models.IntegerField(default=0)
	avatar = models.ImageField(upload_to="Avatars", blank=True)
	subs = models.ManyToManyField(User, default=[], related_name="subs_to")
	achievements = models.ManyToManyField(Achievement, default=[], related_name="achieve_owner")
	activity = models.TextField(default='{}')

	class Meta:
		verbose_name = 'данные пользователя'
		verbose_name_plural = 'данные пользователей'

	def __str__(self):
		return self.user.username


class Post(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to='Post', blank=True)
	date = models.DateTimeField(auto_now_add=True)
	text = models.TextField(max_length=350, blank=True)

	class Meta:
		ordering = ('-date', )
		verbose_name = 'пост'
		verbose_name_plural = 'посты'

	def __str__(self):
		return self.title
