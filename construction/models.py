from django.db import models
from django.contrib.auth.models import User


class Site_User(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    TYPE_ROLE = (
        ('Sitehead', 'Sitehead'),
        ('Superviser', 'Superviser'),
        ('Technician', 'Technician'),
    )
    site_role = models.CharField(max_length=50, choices=TYPE_ROLE)
    image = models.ImageField(upload_to='profile_images/', null=True)

    def __str__(self):
        return str(self.name)


class Construction_Site(models.Model):
    name = models.CharField(max_length=50)
    WORKING_STATUS = (
        ('Working', 'Working'),
        ('Halted', 'Halted'),
        ('Completed', 'Completed'),
    )
    working_status = models.CharField(max_length=50, choices=WORKING_STATUS)
    superviser = models.ManyToManyField(Site_User)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    amount = models.FloatField()
    trans_user = models.ForeignKey(Site_User, on_delete=models.CASCADE)
    TRANSACTION_MEANS = (
        ('Online Payment', 'Online Payment'),
        ('Hard Cash', 'Hard Cash'),
    )
    trans_method = models.CharField(max_length=100, choices=TRANSACTION_MEANS)
    trans_date = models.DateTimeField(auto_now_add=True)
    comments = models.TextField()
    confirmation_status = models.BooleanField(default=False)
    trans_site = models.ForeignKey(
        Construction_Site, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.trans_user) + ' ' + self.comments[:10]

    @property
    def status(self):
        if self.confirmation_status == True:
            status = 'Confirmed'
        else:
            status = 'Not Confirmed'
        return str(status)
