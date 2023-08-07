from django.core.exceptions import ValidationError


def score_validator(score):
    if score > 100 or score < 0:
        raise ValidationError("score must be 0-100")


def link_validator(link: str):
    if not link.startswith("https://www.metacritic.com"):
        raise ValidationError("invalid link ! ")


def rate_validator(rate):
    if rate > 10 or rate < 0:
        raise ValidationError("rate must be 0-10s")
