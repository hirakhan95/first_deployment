from django.http import HttpResponse
from .models import User, Contact


def show_all_users(request):

    users = list(User.objects.values_list())

    res = ''
    for user in users:
        res += f'Name: {user[1]}, Detail:{user[2]} <br><br>'

    res += '<br><br><br><br>'
    res += "<a href='/contacts'>Go to Contacts</a>"

    return HttpResponse(res)


def show_all_contacts(request):
    contacts = list(Contact.objects.values_list())

    res = ''
    for contact in contacts:
        res += f'Name: {contact[1]}, Email:{contact[2]}, Contact:{contact[3]} <br><br>'

    res += '<br><br><br><br>'
    res += "<a href='/'>Go to Users</a>"

    return HttpResponse(res)
