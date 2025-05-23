from modeltranslation.translator import register, TranslationOptions
from .models import Program, Course, Upload, UploadVideo

@register(Program)
class ProgramTranslationOptions(TranslationOptions):
    fields = ('title', 'summary')

@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('title', 'summary')

@register(Upload)
class UploadTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(UploadVideo)
class UploadVideoTranslationOptions(TranslationOptions):
    fields = ('title', 'summary')