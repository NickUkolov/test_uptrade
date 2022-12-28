from django import template
from ..models import MenuItem

register = template.Library()


@register.filter
def active_items(value):
    return value.filter(active=True)


@register.inclusion_tag('menu/menu.html')
def draw_menu(menu_name):

    menu_items = MenuItem.objects.filter(menu__name=menu_name, active=True)
    context = {'items': menu_items,
                     'menu_name': menu_name}

    return context
