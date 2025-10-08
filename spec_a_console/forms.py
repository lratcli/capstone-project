from django import forms  # type: ignore
from .models import ConsoleSystem
from .models import SystemReview


class ConsoleSystemForm(forms.ModelForm):
    class Meta:
        model = ConsoleSystem
        fields = [
            'name',
            'featured_image',
            'manufacturer',
            'release_year',
            'cpu',
            'graphics',
            'memory',
            'launch_rrp_unadjusted',
            'detailed_description',
            'brief_description',
        ]
        widgets = {
            # 'release_year': forms.DateInput(attrs={'type': 'date'}),
            'detailed_description': forms.Textarea(attrs={'rows': 4}),
            'brief_description': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'name': 'Console Name',
            'brief_description': 'Brief Description',
            'release_year': 'Release Year',
            'manufacturer': 'Manufacturer',
            'launch_rrp_unadjusted': 'Launch Price (USD)',
            'detailed_description': 'Technical Specifications',
        }
        help_texts = {
            'launch_rrp_unadjusted': 'Enter the launch price in USD.',
            'release_year': 'Select the release year of the console.',
        }
        error_messages = {
            'name': {
                'max_length': 'The name is too long.',
                'unique': 'A console with this name already exists.',
            },
            'launch_rrp_unadjusted': {
                'invalid': 'Enter a valid price.',
            },
        }


class SystemReviewForm(forms.ModelForm):
    class Meta:
        model = SystemReview
        fields = (
            'rating',
            'comment',
        )
        widgets = {
            'comment': forms.Textarea(attrs={
                'rows': 2,
                'style': 'resize:vertical; width:100%;',
                'oninput':
                "this.style.height='';"
                "this.style.height=this.scrollHeight+'px'"
            }),
        }
