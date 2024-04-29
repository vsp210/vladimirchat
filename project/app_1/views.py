from django.shortcuts import redirect, render
from.models import Messages
from.forms import MessageForm
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta

@login_required
def index(request):
    if Messages.objects.count() > 3:
        Messages.objects.order_by('pub_date').first().delete()

    messages = Messages.objects.all().order_by('-pub_date')[:20]
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.save()
            return redirect('index')
    else:
        form = MessageForm()
    return render(request, 'home.html', {
        'form': form,
        'messages': messages
    })
@login_required
def messages(request):
    messages = Messages.objects.all().order_by('-pub_date')[:20]
    return render(request, 'messages.html', {
        'messages': messages
    })

from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})


from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def delete_message(request, message_id):
    user = request.user.id
    message = get_object_or_404(Messages, id=message_id, author=user)
    print(message)
    message.delete()
    return JsonResponse({'success': True})
