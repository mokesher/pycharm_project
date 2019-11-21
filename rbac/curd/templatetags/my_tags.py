from django import template

register=template.Library()



@register.inclusion_tag("menu.html")
def get_menu(request):
    menu_permission_list = request.session["menu_permission_list"]

    return {"menu_permission_list": menu_permission_list}