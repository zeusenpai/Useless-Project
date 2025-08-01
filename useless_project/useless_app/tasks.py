from celery import shared_task
from django.core.mail import send_mail
from useless_project.settings import EMAIL_HOST_USER
from .services import get_content

@shared_task
def spam_email_task(recipient, repeat_count=10, delay_sec=60):
    for _ in range(repeat_count):
        thought = get_content()
        send_mail(
            "Gemini Deep Thought",
            thought,
            EMAIL_HOST_USER,
            [recipient],
            fail_silently=True,
        )
        # Wait between emails
        import time
        time.sleep(delay_sec)
