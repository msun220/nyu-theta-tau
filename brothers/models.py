from django.db import models


class PledgeClass(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Pledge Class"
        verbose_name_plural = "Pledge Classes"


class Brother(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    brother_number = models.IntegerField()
    major = models.CharField(max_length=200)
    eboard = models.BooleanField(default=False)
    eboard_title = models.CharField(max_length=200, blank=True)
    quote = models.TextField(blank=True)
    grad_year = models.IntegerField()
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    headshot = models.URLField(max_length=500, blank=True, null=True)

    pledge_class = models.ForeignKey(
        "PledgeClass",
        related_name="brothers",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
