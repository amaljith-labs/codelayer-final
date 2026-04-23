from django.shortcuts import render,get_object_or_404

from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactInquiry, JobOpening, BlogPost, TeamMember, Event, GalleryItem, Testimonial, FAQ

# Create your views here.

def home(request):

    posts = BlogPost.objects.filter(is_published=True).order_by('-created_at')
    testimonials = Testimonial.objects.filter(is_published=True)
    faqs = FAQ.objects.filter(is_published=True)

    context = {
        'posts': posts,
        'testimonials': testimonials,
        'faqs': faqs,
    }

    return render(request, 'home.html', context)

def services(request):
    return render(request, 'services.html')

def career(request):

    jobs = JobOpening.objects.filter(is_active=True).order_by('-posted_date')
    context = {'jobs': jobs}

    return render(request, 'career.html', context)

def about(request):
    team = TeamMember.objects.filter(is_visible=True)
    context = {'team': team}

    return render(request, 'about.html', context)

def quarry_crusher(request):
    return render(request, 'quarry_crusher.html')

def ready_mix_erp(request):
    return render(request, 'ready-mix-erp.html')

def brick_erp(request):
    return render(request, 'brick-erp.html')

def blogs(request):
    posts = BlogPost.objects.filter(is_published=True).order_by('-created_at')
    context = {'posts': posts}

    return render(request, 'blogs.html', context)

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)

    return render(request, 'blog_detail.html', {'post': post})

def customerStories(request):
    testimonials = Testimonial.objects.filter(is_published=True)
    context = {'testimonials': testimonials}
    return render(request, 'customer-stories.html', context)

def events(request):
    events = Event.objects.filter(is_active=True)

    return render(request, 'events.html', {'events': events})

def siteVisits(request):
    images = GalleryItem.objects.all()

    return render(request, 'site-visits.html',{'images': images})

def resources(request):
    return render(request, 'resources.html')


def contact(request):
    """
    View to display the contact page and handle AJAX form submissions.
    """
    if request.method == "POST":
        # Extract data from POST (Names must match the 'name' attribute in HTML)
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        company = request.POST.get('company', '').strip()
        req_type = request.POST.get('req_type', 'General Inquiry')
        interests = request.POST.get('interests', '')  # Sent from contactForm.js
        message = request.POST.get('message', '').strip()
        source = request.POST.get('source', '')

        # 1. Server-side Validation
        if not full_name or not email or not message:
            return JsonResponse({
                "status": "error",
                "message": "Required fields are missing."
            }, status=400)

        try:
            # 2. Save Inquiry to the Database (Admin Dashboard)
            inquiry = ContactInquiry.objects.create(
                full_name=full_name,
                email=email,
                phone_number=phone,
                company_name=company,
                requirement_type=req_type,
                interests=interests,
                message=message,
                source=source
            )

            # 3. Prepare and Send Email Notification to Admin
            subject = f"[{req_type.upper()}] New Lead: {full_name}"

            email_body = f"""
            New inquiry received from website:

            Requirement: {req_type}
            Name:        {full_name}
            Email:       {email}
            Phone:       {phone if phone else 'N/A'}
            Company:     {company if company else 'N/A'}

            Interests:   {interests}
            Source:      {source}

            Message:
            {message}

            ---
            View this lead in the admin panel: /admin/
            """

            send_mail(
                subject,
                email_body,
                settings.EMAIL_HOST_USER,  # From (Sender)
                [settings.ADMIN_EMAIL_LIST],  # To (Your Inbox)
                fail_silently=False,
            )

            # 4. Return success response to AJAX
            return JsonResponse({"status": "success"})

        except Exception as e:
            # Log the error for debugging
            print(f"Contact Form Error: {e}")
            return JsonResponse({
                "status": "error",
                "message": "Internal server error. Please try again later."
            }, status=500)

    # For standard page visits (GET request)
    return render(request, 'contact.html')


def quarryLanding(request):
    return render(request, 'quarry-crusher-landing.html')

def readymixLanding(request):
    return render(request, 'ready-mix-landing.html')

def brickLanding(request):
    return render(request, 'brick-landing.html')

def privacy(request):
    return render(request, 'privacy.html')

def term(request):
    return render(request, 'term.html')


def landingLeadCapture(request):
    """
    Unified AJAX handler for all product landing pages.
    """
    if request.method == "POST":
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        company = request.POST.get('company', '').strip()
        product = request.POST.get('product_name', 'Unknown Product')

        if not all([full_name, email, phone, company]):
            return JsonResponse({"status": "error", "message": "All fields are required."}, status=400)

        try:
            # Save to the same ContactInquiry model
            ContactInquiry.objects.create(
                full_name=full_name,
                email=email,
                phone_number=phone,
                company_name=company,
                interests=product,  # This stores 'Quarry & Crusher ERP', etc.
                requirement_type="Request a Demo",
                message=f"Lead generated from {product} landing page.",
                source="Landing Page"
            )

            # Send Notification Email
            subject = f"🔥 NEW LEAD: {product}"
            email_body = f"New Inquiry for {product}\n\nName: {full_name}\nCompany: {company}\nPhone: {phone}\nEmail: {email}"

            send_mail(
                subject,
                email_body,
                settings.EMAIL_HOST_USER,
                [settings.ADMIN_EMAIL_LIST],
                fail_silently=True
            )

            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)