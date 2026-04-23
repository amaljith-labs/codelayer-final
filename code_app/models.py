from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class ContactInquiry(models.Model):
    # Requirement Types (Matches the 'value' in your HTML radio buttons)
    DEMO = 'Request a Demo'
    VISIT = 'Site Visit'
    GENERAL = 'General Inquiry'

    REQUIREMENT_CHOICES = [
        (DEMO, 'Request a Demo'),
        (VISIT, 'Site Visit'),
        (GENERAL, 'General Inquiry'),
    ]

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    interests = models.TextField(help_text="Stored as comma-separated values from chips")
    message = models.TextField()
    source = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    requirement_type = models.CharField(
        max_length=50,
        choices=REQUIREMENT_CHOICES,
        default=GENERAL
    )

    class Meta:
        verbose_name = "Contact Inquiry"
        verbose_name_plural = "Contact Inquiries"
        ordering = ['-created_at']  # Shows newest inquiries at the top

    def __str__(self):
        return f"{self.full_name} ({self.company_name if self.company_name else 'No Company'})"


class JobOpening(models.Model):
    DEPARTMENT_CHOICES = [
        ('engineering', 'Engineering'),
        ('consulting', 'Consulting'),
        ('sales', 'Sales & Marketing'),
        ('support', 'Support'),
    ]

    WORK_MODE_CHOICES = [
        ('On-site', 'On-site'),
        ('Remote', 'Remote'),
        ('Hybrid', 'Hybrid'),
        ('Remote / Hybrid', 'Remote / Hybrid'),
    ]

    title = models.CharField(max_length=255)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    location = models.CharField(max_length=255, default="Thiruvananthapuram, Kerala")
    job_type = models.CharField(max_length=50, default="Full-time")  # e.g. Part-time, Internship
    work_mode = models.CharField(max_length=50, choices=WORK_MODE_CHOICES, default='On-site')
    posted_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.get_department_display()})"


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    featured_image = models.ImageField(upload_to='blog_images/')
    excerpt = models.TextField(max_length=250)
    content = RichTextUploadingField() # This adds the Rich Text Editor
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team_photos/')
    linkedin_url = models.URLField(max_length=500, blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first (e.g., 1 for CEO)")
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name'] # Primary sort by order, secondary by name
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def __str__(self):
        return f"{self.name} - {self.role}"


class Event(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='events/')
    date_text = models.CharField(max_length=100, help_text="Example: April 24, 2026 — 3:00 PM IST")
    description = models.TextField(help_text="A short summary of the event")
    external_link = models.URLField(max_length=500, help_text="LinkedIn URL")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class GalleryItem(models.Model):
    site_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    visit_date = models.DateField()
    image = models.ImageField(upload_to='gallery/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-visit_date']
        verbose_name = "Gallery Item"

    def __str__(self):
        return f"{self.site_name} - {self.location}"


class Testimonial(models.Model):
    author_name = models.CharField(max_length=100)
    author_role = models.CharField(max_length=100, help_text="e.g., CFO, Crestline Industries")
    text = models.TextField()
    stars = models.PositiveSmallIntegerField(default=5, help_text="Enter a value between 1 and 5")
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author_name} - {self.author_role}"

    class Meta:
        ordering = ['-created_at']


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    is_published = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0, help_text="Order in which FAQ appears")

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ['order']

    def __str__(self):
        return self.question