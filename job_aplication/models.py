from django.db import models

class Form(models.Model):
    first_name = models.CharField(max_length=80);
    email = models.EmailField();
    last_name = models.CharField(max_length=80);
    date = models.DateField();
    occupation = models.CharField(max_length=80);

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Address(models.Model):
    # Link each address to a Form
    form = models.ForeignKey(Form, related_name="addresses", on_delete=models.CASCADE)

    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street}, {self.city}"
