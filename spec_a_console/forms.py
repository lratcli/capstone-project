from django import forms  # type: ignore
from .models import ConsoleSystem
from .models import SystemReview


class ConsoleSystemForm(forms.ModelForm):
    """
    A form for creating and editing ConsoleSystem instances.
    Includes validation for non-negative launch price.
    """
    # featured_image = forms.ImageField(required=False)
    launch_rrp_unadjusted = forms.DecimalField(
        min_value=0,
        error_messages={'min_value': 'Price cannot be negative.'}
    )

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
            'featured_image': 'Optional. Note: if editing existing system, '
            'current image will be retained if no new image is uploaded.',
            'launch_rrp_unadjusted': 'Enter launch price in USD. '
            'Negative values not allowed.',
            'release_year': 'Choose release year between 1970 and 2025.',
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
    """
    A form for submitting reviews for a ConsoleSystem.
    """
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
