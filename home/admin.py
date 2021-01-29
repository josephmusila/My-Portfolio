from django.contrib import admin
from .models import Sample,Skill,Language,Image,Overview,Framework,Target

class SkillAdmin(admin.ModelAdmin):
    list_display = ('skills',)

class SampleAdmin(admin.ModelAdmin):
    list_display = ('frontEnd','backEnd',)

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('languages',)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('images',)

class FrameWorkAdmin(admin.ModelAdmin):
    list_display = ('frameworks',)

class TargetAdmin(admin.ModelAdmin):
    list_display = ('Targets',)

class OverViewAdmin(admin.ModelAdmin):
    list_display = ('overview',)


admin.site.register(Skill,SkillAdmin)
admin.site.register(Sample,SampleAdmin)
admin.site.register(Language,LanguageAdmin)
admin.site.register(Image,ImageAdmin)
admin.site.register(Overview,OverViewAdmin)
admin.site.register(Framework,FrameWorkAdmin)
admin.site.register(Target,TargetAdmin)

