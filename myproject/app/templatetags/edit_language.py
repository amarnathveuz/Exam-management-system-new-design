from django import template

register = template.Library()

from app.models import Main_exam_language


@register.filter(name='check_edit_language')
def check_edit_language(value,args):
    data = Main_exam_language.objects.filter(Exam_id=value)
    list1 = []
    for i in data:
        list1.append(i.language_access)
    if args in list1:
        return True