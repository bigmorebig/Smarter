from django.shortcuts import render
from .models import UserMessage

# Create your views here.
def get_form(request):
    # all_messages = UserMessage.objects.filter(passwd='123456')
    # for message in all_messages:
    #     print(message.user)
    user_message = UserMessage()
    user_message.user = '胖胖'
    user_message.phone_num = '123456'
    user_message.passwd = '123456'
    user_message.confirm_passwd = '123456'
    user_message.object_id = '123456'
    user_message.verfication_code = '456'
    user_message.save()
    return render(request, 'message_form.html')