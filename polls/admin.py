from django.contrib import admin
from .models import Choice, Question


# Register your models here.


# class ChoiceInLine(admin.StackedInline):
#     model = Choice
#     extra = 3

# With that TabularInline (instead of StackedInline),
# the related objects are displayed in a more compact, table-based format
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


admin.site.register(Choice)


# By registering the Question model with admin.site.register(Question),
# Django was able to construct a default form representation.
# Often, you’ll want to customize how the admin form looks and works.
# You’ll do this by telling Django the options you want when you register the object.

# admin.site.register(Question)

# This particular change above makes the “Publication date” come before the “Question” field
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']})
#     ]

# This tells Django: “Choice objects are edited on the Question admin page.
# By default, provide enough fields for 3 choices.”
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInLine]
    # By default, Django displays the str() of each object.
    # But sometimes it’d be more helpful if we could display individual fields.
    # To do that, use the list_display admin option,
    # which is a tuple of field names to display, as columns, on the change list page for the object:
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # That adds a “Filter” sidebar that lets people filter the change list by the pub_date field:
    list_filter = ['pub_date']


admin.site.register(Question, QuestionAdmin)
