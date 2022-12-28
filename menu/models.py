from django.db import models
from django.core.exceptions import ValidationError


class Menu(models.Model):

    name = models.CharField(verbose_name='name', max_length=255)

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menu'
        ordering = ['name']

    def __str__(self):
        return self.name


class MenuItem(models.Model):

    name = models.CharField(max_length=255, verbose_name='name')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items', verbose_name='menu item')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                               verbose_name='parent')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="url")
    active = models.BooleanField(default=True, verbose_name='active')

    class Meta:
        verbose_name = 'menu position'
        verbose_name_plural = 'menu positions'
        ordering = ['name']

    def clean(self):
        if self.parent is None:
            return super
        if self.menu != self.parent.menu:
            raise ValidationError(
                {'parent': f"Element and its parent should be in same menu. Parent's menu: {self.parent.menu}"}
            )

    def __str__(self):
        return self.name
