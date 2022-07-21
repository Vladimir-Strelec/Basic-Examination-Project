from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator


def valid_only_character(value):
    if not value.isalpha():
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):

    PROFILE_NAME_MAX_LENGTH = 15
    PROFILE_NAME_MIN_LENGTH = 2

    MIN_VALUE_AGE = 1

    user_name = models.CharField(
        max_length=PROFILE_NAME_MAX_LENGTH,
        validators=(MinLengthValidator(PROFILE_NAME_MIN_LENGTH),
                    valid_only_character,
                    ),
    )

    email = models.EmailField()

    age = models.IntegerField(
        default=0,
        null=True,
        blank=True,
        validators=(MinValueValidator(MIN_VALUE_AGE),),
    )


class Album(models.Model):
    MAX_LENGTH_GENRE = 30
    MIN_VALUE_PRICE = 1

    Pop_Music = 'Pop Music'
    Jazz_Music = 'Jazz Music'
    R_and_B_Music = 'R&B Music'
    Rock_Music = 'Rock Music'
    Country_Music = 'Country Music'
    Dance_Music = 'Dance Music'
    Hip_Hop_Music = 'Hip Hop Music'
    Other = 'Other'
    ALL_MUSIC = [(x, x) for x in (Pop_Music, Jazz_Music, R_and_B_Music, Rock_Music,
                                  Country_Music, Dance_Music, Hip_Hop_Music, Other)]

    name = models.CharField(
        max_length=MAX_LENGTH_GENRE
    )

    artist = models.CharField(
        max_length=MAX_LENGTH_GENRE
    )

    genre = models.CharField(
        max_length=MAX_LENGTH_GENRE,
        choices=ALL_MUSIC,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image = models.URLField()

    price = models.FloatField(
        default=0,
        validators=(MinValueValidator(MIN_VALUE_PRICE),),
    )
