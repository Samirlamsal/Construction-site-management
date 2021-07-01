from django.db import models
from django.contrib.auth.models import User


class Site_User(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100, null=True, blank=True)
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
    image = models.ImageField(
        upload_to="site_profiles/",  null=True, blank=True)
    num_workers = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(null=True, blank=True)
    expensed = models.IntegerField(null=True, blank=True)
    WORKING_STATUS = (
        ('Working', 'Working'),
        ('Halted', 'Halted'),
        ('Completed', 'Completed'),
    )
    working_status = models.CharField(max_length=50, choices=WORKING_STATUS)
    location = models.CharField(max_length=100, null=True, blank=True)
    superviser = models.ForeignKey(
        Site_User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    amount = models.FloatField()
    trans_user = models.ForeignKey(Site_User, on_delete=models.CASCADE)
    TRANSACTION_MEANS = (
        ('Online Payment', 'Online Payment'),
        ('Hard Cash', 'Hard Cash'),
    )
    TRANSACTION_TYPE = (
        ('Debit', 'Debit'),
        ('Credit', 'Credit'),
    )

    trans_method = models.CharField(max_length=100, choices=TRANSACTION_MEANS)
    trans_type = models.CharField(
        max_length=50, choices=TRANSACTION_TYPE,  null=True, blank=True)
    trans_date = models.DateTimeField(auto_now_add=True)
    comments = models.TextField()
    confirmation_status = models.BooleanField(default=False)
    trans_site = models.ForeignKey(
        Construction_Site, on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(
        upload_to='transactionimages/', null=True, blank=True)

    def __str__(self):
        return str(self.trans_user) + ' ' + self.comments[:10]

    @property
    def status(self):
        if self.confirmation_status == True:
            status = 'Confirmed'
        else:
            status = 'Not Confirmed'
        return str(status)
