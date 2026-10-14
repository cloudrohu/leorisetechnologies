from admin_thumbnails import settings
from django.contrib import admin
from .models import settings

# Register your models here.

@admin.register(settings)
class SettingsAdmin(admin.ModelAdmin):

    list_display = (
        "site_name",
        "phone_number",
        "email",
    )

    search_fields = (
        "site_name",
        "email",
        "phone_number",
    )

    fieldsets = (

        # ─────────────────────────────
        # BASIC INFORMATION
        # ─────────────────────────────
        (
            "🏠 Basic Information",
            {
                "fields": (
                    "site_name",
                    "logo",
                    "favicon",
                    "offer_banner",
                )
            }
        ),

        (
            "🔍 SEO & Meta Information",
            {
                "fields": (
                    "meta_title",
                    "meta_description",
                    "meta_keywords",
                    "meta_author",
                    "og_title",
                    "og_description",
                    "og_image",
                )
            }
        ),

        (
            "🎴 Card Design",
            {
                "fields": (
                    "front_view_card",
                    "back_view_card",
                    "alternate_design_card",
                )
            }
        ),

        (
            "📱 Social Media",
            {
                "fields": (
                    "facebook_url",
                    "twitter_url",
                    "instagram_url",
                    "youtube_url",
                    "linkedin_url",
                )
            }
        ),

        (
            "📞 Contact Information",
            {
                "fields": (
                    "phone_number",
                    "email",
                    "address",
                    "google_iframe",
                )
            }
        ),

        (
            "🦶 Footer Information",
            {
                "fields": (
                    "footer_text",
                    "copyright",
                )
            }
        ),
    )

    # Only one settings record
    def has_add_permission(self, request):
        return not settings.objects.exists()