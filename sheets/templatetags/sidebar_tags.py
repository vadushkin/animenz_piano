from django import template

from sheets.models import Tag, Sheet, Category

register = template.Library()


@register.simple_tag(name='get_count_tags')
def get_count_tags():
    return Tag.objects.count()


@register.simple_tag(name='get_count_archives')
def get_count_archives():
    return Sheet.objects.count()


@register.simple_tag(name='get_count_categories')
def get_count_categories():
    return Category.objects.count()
