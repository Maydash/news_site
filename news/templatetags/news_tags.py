from django import template
from news.models import Category
from django.db.models import Count


register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()
    # return Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    # categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    # print(categories)
    # return {'categories': categories}



# @register.inclusion_tag('inc/_sidebar.html')
# def show_categories():
#     categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
#     return {'categories': categories}

