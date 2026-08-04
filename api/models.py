from django.contrib.auth.models import User
from django.db import models


class UserSession(models.Model):
  user = models.ForeignKey(
      User, on_delete=models.CASCADE, verbose_name="Пользователь"
  )
  session_key = models.CharField(
      max_length=255, unique=True, verbose_name="Ключ сессии (Redis)"
  )
  ip_address = models.GenericIPAddressField(
      verbose_name="IP-адрес"
  )
  user_agent = models.TextField(verbose_name="Информация об устройстве")
  created_at = models.DateTimeField(
      auto_now_add=True, verbose_name="Время входа"
  )
  is_active = models.BooleanField(default=True, verbose_name="Активна")

  def __str__(self):
    return f"Сессия {self.user.username} ({self.ip_address})"

  class Meta:
    verbose_name = "Сессия пользователя"
    verbose_name_plural = "Сессии пользователей"