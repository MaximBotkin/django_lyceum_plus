from django import template
import math


register = template.Library()


@register.filter("input_type")
def input_type(ob):
    """
    Extract form field type
    :param ob: form field
    :return: string of form field widget type
    """
    return ob.field.widget.__class__.__name__


@register.filter(name="add_classes")
def add_classes(value, arg):
    """
    Add provided classes to form field
    :param value: form field
    :param arg: string of classes seperated by ' '
    :return: edited field
    """
    css_classes = value.field.widget.attrs.get("class", "")
    # check if class is set or empty and split its content to list (or init list)
    if css_classes:
        css_classes = css_classes.split(" ")
    else:
        css_classes = []
    # prepare new classes to list
    args = arg.split(" ")
    for a in args:
        if a not in css_classes:
            css_classes.append(a)
    # join back to single string
    return value.as_widget(attrs={"class": " ".join(css_classes)})


@register.filter(name="divide")
def divide(value, arg):
    """Divide list on sublists with length = arg"""
    result = []
    for i in range(0, math.ceil(len(value) / 4)):
        result.append(value[arg * i : arg * (i + 1)])
    return result
