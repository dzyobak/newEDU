from modeltranslation.translator import register, TranslationOptions
from .models import Quiz, Question, MCQuestion, EssayQuestion, Choice


@register(Quiz)
class QuizTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = ('content', 'explanation')


@register(MCQuestion)
class MCQuestionTranslationOptions(TranslationOptions):
    pass


@register(EssayQuestion)
class EssayQuestionTranslationOptions(TranslationOptions):
    pass


@register(Choice)
class ChoiceTranslationOptions(TranslationOptions):
    fields = ('choice_text',)
