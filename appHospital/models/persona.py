
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

from mailbox import NoSuchMailboxError
from .rol import rolModel


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('El usuario no existe')

        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class personaModel(AbstractBaseUser, PermissionsMixin):
    id = models.IntegerField(primary_key=True);
    username = models.CharField('Username', max_length = 15, unique=True);
    password = models.CharField('Password',max_length=100);
    nombre = models.CharField('Nombre',max_length=15);
    apellido = models.CharField('Apellido',max_length=15);
    edad = models.SmallIntegerField();
    id_rol = models.ForeignKey(rolModel, on_delete=models.RESTRICT);

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username'

