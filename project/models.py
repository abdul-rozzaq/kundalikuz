import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

month_names = ['Yanvar', 'Fevral', 'Mart', 'Aprel', 'May', 'Sentyabr', 'Oktyabr', 'Noyabr', 'Dekabr']
week_days = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba', 'Yakshanba']

class Day(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()


    def __str__(self) -> str:
        
        
        return self.date.strftime(f"{week_days[self.date.weekday()]} %d {month_names[self.date.month - 1]}. %Y")
    


class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.created_at.strftime("%H:%M")
    
    