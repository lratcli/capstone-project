from django.db import models  # type: ignore
from django.contrib.auth.models import User  # type: ignore
from cloudinary.models import CloudinaryField  # type: ignore
from django.core.validators import MinValueValidator  # type: ignore
from django.core.validators import MaxValueValidator  # type: ignore


# Create your models here.


STATUS_CHOICES = (
    (0, 'Submitted'),
    (1, 'Accepted'),
)


class ConsoleSystem(models.Model):
    """
    A model to represent a hypothetical gaming console created by
        :model:`auth.User`.

    Related to :model:`auth.User` and :model:`spec_a_console.SystemReview`
    """

    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='console_systems')
    featured_image = CloudinaryField('image', default='placeholder')

    manufacturer = models.CharField(max_length=200)
    release_year = models.IntegerField(
        validators=[MinValueValidator(1970), MaxValueValidator(2025)],
        help_text="Enter the year your hypothetical console was introduced"
    )
    cpu = models.CharField(max_length=200)
    graphics = models.CharField(max_length=200)
    memory = models.CharField(max_length=200)
    launch_rrp_unadjusted = models.DecimalField(
        max_digits=10, decimal_places=2)

    detailed_description = models.TextField()
    brief_description = models.TextField(max_length=300)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    approval = models.IntegerField(choices=STATUS_CHOICES, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name


class SystemReview(models.Model):
    """
    A model to represent user reviews for a ConsoleSystem.
    Related to :model:`auth.User` and :model:`spec_a_console.ConsoleSystem`
    """
    system = models.ForeignKey(
        ConsoleSystem, on_delete=models.CASCADE, related_name='reviews'
    )
    reviewer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='system_reviewer')
    rating = models.PositiveSmallIntegerField(
        choices=[(i, str(i)) for i in range(1, 11)],
        help_text="Rating from 1 (worst) to 10 (best)"
    )
    comment = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.reviewer.username} review of {self.system.name}"
