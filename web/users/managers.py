from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email обязателен.")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if not extra_fields.get("is_staff") or not extra_fields.get("is_superuser"):
            raise ValueError(
                "Cуперпользователь обязан иметь поля is_staff и is_superuser."
            )

        return self.create_user(email, password, **extra_fields)

    def get_all_active_users(self):
        return self.filter(is_active=True)

    def get_user_page(self, user_id):
        return self.filter(pk=1)
