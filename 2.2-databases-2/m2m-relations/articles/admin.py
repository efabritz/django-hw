from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        check_main = 0
        for form in self.forms:
            if form.cleaned_data and form.cleaned_data['is_main']:
                check_main += 1
            if check_main > 1:
                raise ValidationError('Разрешен только один основной тэг')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticletAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'published_at', 'image',)
    inlines = [RelationshipInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [RelationshipInline]
