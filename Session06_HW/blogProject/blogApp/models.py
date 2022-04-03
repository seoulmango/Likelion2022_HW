from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    #PK (ID) 값은 자동으로 1부터 시작해서 입력되므로 따로 쓸 필요 없다.
    title = models.CharField(max_length=200)
    content = models.TextField()

    coding='co'
    hobby='ho'
    food='fo'
    category_choices = [
        (coding, 'coding'),
        (hobby, 'hobby'),
        (food, 'food'),
        ('no', 'no'),
    ]
    category = models.CharField(
        max_length = 2,
        choices = category_choices,
    )
    time_created = models.DateTimeField(default=timezone.now)
    time_updated = models.DateTimeField(blank=True, null=True)

    def update_date(self):
        self.time_updated = timezone.now()
        self.save()

    def __str__(self):
        return self.title