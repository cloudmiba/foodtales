from django.contrib import admin
from .models import Receipt
from .models import ReceiptIngredient
from .models import IngredientMeta
from .models import QuantityUnit
from .models import Category

admin.site.register(Receipt)
admin.site.register(ReceiptIngredient)
admin.site.register(IngredientMeta)
admin.site.register(QuantityUnit)
admin.site.register(Category)