from django.contrib import admin
from .models import Post, Category, Tag

# Register your model

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_field = {'slug': ('name', )}
    
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name', )}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at', 'published_at', 'is_published')
    list_filter = ('is_published', 'author', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}#tells the admin: "auto-generate the slug field's value from the title field, live, as the user types."
    date_hierarchy = 'published_at' #adds a drill-down date navigation bar at the top of the admin's post list — showing years, then clicking a year shows months, then days.
    ordering = ('-published_at',) #The - prefix means descending order. So -published_at = newest posts first. Without the -, it'd sort oldest first.
    filter_horizontal = ('tags',)