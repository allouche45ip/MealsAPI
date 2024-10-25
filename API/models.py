

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import UniqueConstraint, Index
# ruba  الوجبة
class Meal(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

    def __str__(self):
        return self.title

# تقيم الوحبة 
# من طرف الوحبة   foreign key  Meal   الوحبة 
# user    --->   جبناه عن طرف  import user   par defualte
class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])  #  تقيم الوحبة 1...5

    # def __str__(self):
    #     return self.meal


    class Meta:
      #  unique_together = (('user', 'meal'),)  #   تقيم اكثر من مره  user لايمكن   unique_together
      #  index_together = (('user', 'meal'),)

        constraints = [
            UniqueConstraint(fields=['user', 'meal'], name='unique_user_meal')
        ]
        indexes = [
            Index(fields=['user', 'meal']),
        ]