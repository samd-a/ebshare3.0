from django import template

register = template.Library()

#points per time
@register.filter
def ppt(btnNum, book_points):
    return float(book_points) * (1 + (btnNum * 1.5))
#seconds purchasable
@register.filter
def secsP(btnNum, secs):
    btnNum = btnNum + 1
    return btnNum  * btnNum * float(secs)
