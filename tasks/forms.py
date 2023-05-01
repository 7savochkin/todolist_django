from django import forms

from tasks.models import TaskBook


class CreateTaskBookForm(forms.ModelForm):

    class Meta:
        model = TaskBook
        fields = ('title', 'description', 'expired_date', 'user')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': ' '}),
            'description': forms.TextInput(attrs={'placeholder': ' '}),
            'expired_date': forms.DateInput(attrs={'placeholder': ' '}),
            'user': forms.HiddenInput(attrs={'placeholder': ' '}),
        }

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def clean(self):
        breakpoint()
