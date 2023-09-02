from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class JobTitle(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    name = models.CharField(max_length=75, unique=True, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado em')

    def __str__(self):
        return self.name


class Profile(models.Model):
    '''Perfil do usuário'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))
    job_title = models.ForeignKey(JobTitle, related_name='list_profiles', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('Job Title'))
    workload = models.PositiveSmallIntegerField(default=40, verbose_name=_('Workload'))
    wage = models.PositiveSmallIntegerField(default=3000, verbose_name=_('Wage'))
    engineering_team = models.BooleanField(default=True, verbose_name=_('Engineering team'))

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def __str__(self):
        return f'{_("Profile")} - { self.user.username }'


@receiver(post_save, sender=User)
def post_save_user_signal(sender, instance, created=False, *args, **kwargs):
    '''Adiciona perfil usuário após adição no servidor'''
    if created:
        Profile.objects.create(
            user=instance,
        )
