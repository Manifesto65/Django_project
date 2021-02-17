from django import template

register = template.Library()

@register.filter(name = 'currency')
def currency(num):
    return "Rs. "+ str(num)

@register.filter(name = 'order_total_price')
def order_total_price(order):
    return order.product.price * order.quantity