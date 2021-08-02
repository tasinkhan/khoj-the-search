from django.db import models
from django.core.validators import validate_comma_separated_integer_list
from Usermodule.models import CustomUser

# Create your models here.

class Search(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    input_values = models.CharField(validators=[validate_comma_separated_integer_list], max_length=30, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Searches"
    def __str__(self):
        return self.input_values