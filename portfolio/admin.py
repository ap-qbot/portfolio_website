from django.contrib import admin
from .models import Category, Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'button_type', 'created_at')
    list_filter = ('category', 'button_type')
    search_fields = ('title', 'description')

    fieldsets = (
        (None, {
            'fields': ('category', 'title', 'subtitle', 'description', 'image')
        }),
        ('Button Configuration', {
            'fields': ('button_type', 'demo_link', 'youtube_video_id'),
            'classes': ('show',)
        }),
        ('Additional Information', {
            'fields': ('link',)
        })
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['youtube_video_id'].help_text = (
            "Enter only the video ID from the YouTube URL. "
            "Example: for https://www.youtube.com/watch?v=dQw4w9WgXcQ, enter 'dQw4w9WgXcQ'"
        )
        return form


admin.site.register(Category)