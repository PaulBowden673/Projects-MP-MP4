from django.conf import settings
from django.shortcuts import render, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.views import generic
from django.views.generic import TemplateView
from .forms import ContactForm

# Create your views here.


def index(request):
    """ A view to return index page """

    return render(request, 'home/index.html')


class AboutView(TemplateView):
    template_name = "home/about.html"


class LoseweightView(TemplateView):
    template_name = "home/lose-weight.html"


class GainweightView(TemplateView):
    template_name = "home/gain-weight.html"


class EnduranceView(TemplateView):
    template_name = "home/endurance.html"


class LivehealthyView(TemplateView):
    template_name = "home/live-healthy.html"


class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = "home/contact.html"

    def get_success_url(self):
        return reverse("contact")

    def form_valid(self, form):
        """"Getting clean data from the form and creating
        a message to get sent to default email."""
        messages.success(self.request,
                         "Thank you for getting in touch with us. We have received your message.")
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')

        full_message = f"""
        Received message below from {name}, {email}
        ___________________________
        {message}
        """
        send_mail(
            subject="Message from Maximum Effort contact form",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL]
        )
        return super(ContactView, self).form_invalid(form)

