from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name

    def register(self):
        self.save()

    def isExist(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email) #Here get will only give one object while if we use filter it will give a list
        except:
            return False