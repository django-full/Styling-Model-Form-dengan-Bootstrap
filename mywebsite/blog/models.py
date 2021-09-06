from django.db import models

# Create your models here.
class postmodel(models.Model):
    judul = models.CharField(max_length=100)
    body  = models.TextField()
    autor = models.CharField(max_length=200)
    pilihan = (
        ('jurnal','jurnal'),
        ('gosip', 'gosip'),
        ('viral', 'viral'),
    )

    category = models.CharField(
        choices=pilihan,
        max_length=25,
        default='gosip'
    )

    def __str__(self):
        return self.judul
