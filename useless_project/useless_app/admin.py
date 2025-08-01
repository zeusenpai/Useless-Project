from django.contrib import admin
from .models import GeneratedThought
from .services import get_content

@admin.register(GeneratedThought)
class GeneratedThoughtAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'content')
    actions = ['generate_new_thought']

    def generate_new_thought(self, request, queryset):
        content = get_philosophical_content()
        GeneratedThought.objects.create(content=content)
        self.message_user(request, "New philosophical content generated.")
    generate_new_thought.short_description = "Generate new Gemini philosophical content"
