from django import forms

from contest.models import Answer, Contest, Question


class ContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = ['name', 'coefficient', 'start_time', 'end_time', 'author',]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['contest', 'content', 'image', 'difficult_level', 'is_select_multiple',]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['question', 'content', 'image', 'is_correct',]
