from django import template
register = template.Library()
from setpassword.models import Token
import ast, datetime
@register.filter
def toObj(obj, key=False):
    if key == False:
        return ast.literal_eval(obj)
    else:
        return ast.literal_eval(obj).get(key)
        
@register.filter
def count(obj):
    n = 0
    if obj is not None:
        a = ast.literal_eval(obj)
        for x in a:
    	    n += 1
    return n

@register.simple_tag
def delete_token_password():
    now = datetime.datetime.now()
    now = int(now.timestamp())
    o = Token.objects.all()
    for x in o:
        if now > int(x.expired):
            Token.objects.filter(token=x.token).delete()
    return ""
