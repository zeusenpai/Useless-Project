from django.shortcuts import render
from django.http import HttpResponse
from .services import get_content
from django.core.mail import send_mail
from useless_project.settings import EMAIL_HOST_USER
import re

# Create your views here.

def send_email_view(request):
    message = ""
    if request.method == "POST":
        recipient = request.POST.get("recipient", "").strip()
        
        # Simple email validation pattern
        email_regex = r"(^[\w\.\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$)"
        if not re.match(email_regex, recipient):
            message = "Please enter a valid Gmail address."
        elif not recipient.endswith("@gmail.com"):
            message = "Only Gmail addresses are allowed as recipients."
        else:
            thought = get_content()
            subject = "Your Gemini Deep Thought"
            send_mail(
                subject,
                thought,
                EMAIL_HOST_USER,
                [recipient],
                fail_silently=False,
            )
            message = f"Gemini-generated thought sent successfully to {recipient}!"
    
    return render(request, "useless_app/send_email_form.html", {"message": message})