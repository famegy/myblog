from django.contrib import admin
from .models import Post 

# Register your model
@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at', 'published_at', 'is_published')
    list_filter = ('is_published', 'author', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}#tells the admin: "auto-generate the slug field's value from the title field, live, as the user types."
    date_hierarchy = 'published_at' #adds a drill-down date navigation bar at the top of the admin's post list — showing years, then clicking a year shows months, then days.
    ordering = ('-published_at',) #The - prefix means descending order. So -published_at = newest posts first. Without the -, it'd sort oldest first.