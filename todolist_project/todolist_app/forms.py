from django import forms
from .models import TodoItem

class TodoItemForm(forms.ModelForm):
    class Meta:
        model=TodoItem
        fields=['date','time','notes']

class MarkAsCompletedForm(forms.ModelForm):
    class Meta:
        model=TodoItem
        fields=['completed']
        widgets={
            'completed':forms.HiddenInput()
        }