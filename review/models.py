from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from lib.validator import rate_validator


from games.models import Game

User = get_user_model()


class Rate(models.Model):
    game = models.ForeignKey(Game, related_name="rates", on_delete=models.CASCADE, verbose_name=_("Game"))
    user = models.ForeignKey(User, related_name="rates", on_delete=models.CASCADE, verbose_name=_("User"))
    rate = models.PositiveIntegerField(_("Rate"), validators=[rate_validator])
    
    class Meta:
        unique_together = ["user", "game"]
    
class Comment(models.Model):
    game = models.ForeignKey(Game, related_name="comments", on_delete=models.CASCADE, verbose_name=_("Game"))
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE, verbose_name=_("User"))
    content = models.TextField(_("Content"))
    time = models.DateField(auto_now_add=True)
    
    # class Meta:
    #     unique_together = ["user", "game"]