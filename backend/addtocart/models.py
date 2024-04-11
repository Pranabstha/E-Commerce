import uuid
from django.utils import timezone
from django.db import models
from authentication import models as userAuthModel
from items import models as ItemModel

# Create your models here.
class Cart(models.Model):
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Cart identifier')
    item_name = models.ForeignKey(ItemModel.Items, on_delete= models.CASCADE, blank=False, null=False)
    user = models.ForeignKey(userAuthModel.User, on_delete=models.CASCADE, blank=True, null= True)
    quantity = models.IntegerField(default=0)
    cart_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'cart'
        verbose_name_plural = 'Add to cart'

    def __str__(self):
        return str(self.item_name)