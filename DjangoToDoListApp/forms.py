from django.forms import ModelForm, TextInput, ValidationError
from DjangoToDoListApp.models import ToDoItem


class ToDoItemCreateForm(ModelForm):
    class Meta:
        model = ToDoItem
        fields = ('item_text', 'description')
        labels = {
            'item_text': 'Item name',
            'description': 'Description'
        }
        widgets = {
            'item_text': TextInput(attrs={'class': 'form-control'}),
            'description': TextInput(attrs={'class': 'form-control'})
        }

    # Return data in this method will be use to validat
    def clean_item_text(self):
        item_text = self.cleaned_data.get('item_text')
        if len(item_text) > 200:
            raise ValidationError("Maximum length is 100 char")
        elif len(item_text) == 0:
            raise ValidationError("This field is required")
        return item_text

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) > 500:
            raise ValidationError("Maximum length is 100 char")
        elif len(description) == 0:
            raise ValidationError("This field is required")
        return description