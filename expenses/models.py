import uuid

from django.db import models


class Expense(models.Model):
    sno = models.AutoField(primary_key=True)
    added_person = models.CharField(max_length=255)
    added_amount = models.DecimalField(max_digits=10, decimal_places=2)
    added_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"{self.added_person} - {self.added_amount} on {self.added_date}"

