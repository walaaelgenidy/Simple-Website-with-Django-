from django.db import models


# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, db_column="Full name")
    image = models.CharField(max_length=100)
    # birthdate = models.DateField()
    masters = models.BooleanField(null=True)
    cost = models.CharField(max_length=100, null=True)
    details = models.CharField(max_length=1000)
    gender = models.CharField(
        max_length=2,
        choices=[
            ("m", "male"),
            ("f", "female")
        ]
    )

    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    Email = models.EmailField(null=True)

    dept = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
