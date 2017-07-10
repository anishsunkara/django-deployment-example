from django import template

register = template.Library()


@register.filter(name="cuts")
def cuts(value, arg):
    """
    This cuts out all values of "arg" from the string
    :param value:
    :param arg:
    :return:
    """
    return value.replace(arg, "")

# register.filter("cuts", cuts)  # Register the function filter, and use the name first and then the name of the func

