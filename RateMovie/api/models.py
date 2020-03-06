from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Movie(models.Model):
    """Create Save a movie into the database"""
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=360)

    def no_of_ratings(self):
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            sum += rating.stars

        if len(ratings) > 0:
            return sum / len(ratings)
        return 0


    def __str__(self):
        return self.title


class Rating(models.Model):
    """Add a new rating to a movie and saves it into the database"""
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (("user", "movie"),)
        index_together = ( ("user", "movie"),)


    def __str__(self):
        return self.stars
    