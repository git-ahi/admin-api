from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group

# Create your models here.


class MyAccountManager(BaseUserManager):
    """defines the methods to manage the custom user to be created

    Args:
        BaseUserManager ([type]): [description]

    Returns:
        [type]: [description]
    """

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have and email address")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """This will define the custom user model to be used

    Args:
        AbstractBaseUser ([type]): [description]
    """

    email = models.EmailField(verbose_name="email",
                              max_length=100, unique=True)

    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30)
    national_id = models.IntegerField(
        verbose_name="National Id or passport", null=True)
    date_joined = models.DateTimeField(
        verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def delete_user(self):
        self.delete()
