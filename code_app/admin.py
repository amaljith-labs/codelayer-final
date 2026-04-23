# old way
from django.contrib import admin

from .models import ContactInquiry, JobOpening,BlogPost, TeamMember, Event, GalleryItem, Testimonial, FAQ
from django.utils.html import format_html


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    # Columns shown in the list view
    list_display = ('priority_status', 'full_name', 'company_name', 'email', 'created_at')

    # Filters on the right side
    list_filter = ('requirement_type', 'source', 'created_at')

    # Search bar functionality
    search_fields = ('full_name', 'email', 'company_name', 'message')

    # Make fields read-only so they can't be accidentally changed
    readonly_fields = ('created_at',)

    # Custom colored tag for the Requirement Type
    def priority_status(self, obj):
        colors = {
            'Request a Demo': '#1ec8a0',  # Green
            'Site Visit': '#ff9800',  # Orange
            'General Inquiry': '#6b8580',  # Grey
        }
        color = colors.get(obj.requirement_type, '#6b8580')
        return format_html(
            '<span style="background: {}; color: white; padding: 3px 10px; border-radius: 12px; font-size: 11px; font-weight: bold;">{}</span>',
            color,
            obj.requirement_type
        )

    priority_status.short_description = 'Type'



@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'work_mode', 'is_active', 'posted_date')
    list_filter = ('department', 'work_mode', 'is_active')
    search_fields = ('title',)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'order', 'is_visible')
    list_editable = ('order', 'is_visible') # Allows you to change order quickly
    list_filter = ('is_visible',)
    search_fields = ('name', 'role')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_text', 'is_active')
    search_fields = ('title', 'description')
    list_editable = ('is_active',)


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'location', 'visit_date')
    list_filter = ('visit_date', 'location')
    search_fields = ('site_name', 'location')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'author_role', 'stars', 'is_published')
    list_filter = ('is_published', 'stars')
    search_fields = ('author_name', 'author_role', 'text')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    # 'order' is displayed so you can see the sequence
    list_display = ('question', 'order', 'is_published')
    list_editable = ('order', 'is_published')
    search_fields = ('question', 'answer')
    # Sort by order by default in admin
    ordering = ('order',)