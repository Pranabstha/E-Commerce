import uuid
from django.utils import timezone
from django.db import models
from authentication import models as userAuthModel

# Create your models here.
# asd
class Items(models.Model):
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='items identifier')
    item_name = models.CharField(max_length = 50)
    item_description = models.CharField(max_length = 255)
    item_category = models.CharField(max_length = 50)
    item_price = models.IntegerField()
    item_image = models.ImageField(upload_to='items_image')
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(userAuthModel.User, on_delete=models.CASCADE, blank=True, null= True)

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'

    def __str__(self):
        return self.item_name + ' | ' + self.item_category