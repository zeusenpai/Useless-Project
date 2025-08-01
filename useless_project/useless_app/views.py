from django.shortcuts import render
from .services import get_content
from django.core.mail import send_mail
from useless_project.settings import EMAIL_HOST_USER
import time
import re

# Create your views here.

def send_email_view(request):
    message = ""
    if request.method == "POST":
        recipient = request.POST.get("recipient", "").strip()
        count = int(request.POST.get("count", "1"))
        count = min(max(count, 1), 20)
        delay = int(request.POST.get("delay", 30))
        delay = min(max(delay, 1), 3600)
        
        # Simple email validation pattern
        email_regex = r"(^[\w\.\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$)"
        if not re.match(email_regex, recipient):
            message = "Please enter a valid Gmail address."
        elif not recipient.endswith("@gmail.com"):
            message = "Only Gmail addresses are allowed as recipients."
        else:
            for _ in range(count):
                thought = get_content()
                send_mail(
                    "HeHeHe!!!!",
                    thought,
                    EMAIL_HOST_USER,
                    [recipient],
                    fail_silently=True,  # Use False for debugging
                )
                time.sleep(delay)
            message = f"Spamming {recipient} with {count} Gemini thoughts, one every {delay} seconds!"
    
    return render(request, "useless_app/spam_email_form.html", {"message": message})