from django.db import models

class Guest(models.Model):
    group_choices = (
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Ms', 'Ms'),
    )
    priority_choices = (
        ('First', 'First'),
        ('Second', 'Second'),
        ('Third', 'Third'),
    )
    inviter_choices = (
        ('Groom', 'Groom'),
        ('Bride', 'Bride'),
    )
    name = models.CharField(max_length=50)
    group = models.CharField(max_length=5, choices=group_choices, default='Mr')
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    priority = models.CharField(max_length=10, choices=priority_choices, default='Third')
    inviter = models.CharField(max_length=10, choices=inviter_choices, default='Groom')
    estimate = models.PositiveIntegerField(default=2)
    
    def __unicode__(self):
        return self.name