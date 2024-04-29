from django import forms
from .models import Messages

class MessageForm(forms.ModelForm):
    text = forms.CharField(required=False)

    class Meta:
        model = Messages
        fields = ['text', 'images']
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Type your message here...'}),
        }
        labels = {
            'text': '',
        }
        # Remove 'text' from the required fields
        required = ('images',)

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if not text and not self.cleaned_data.get('images'):
            raise forms.ValidationError('Message cannot be empty')
        return text
