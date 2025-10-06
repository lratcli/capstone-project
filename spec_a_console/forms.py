from django import forms
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
#        widgets = {
#            'review_date': forms.DateInput(attrs={'type': 'date'}),
#            'review_text': forms.Textarea(attrs={'rows': 4}),
#        }
#        labels = {
#            'console': 'Console Reviewed',
#            'reviewer_name': 'Reviewer Name',
#            'rating': 'Rating (1-10)',
#            'review_text': 'Review Text',
#            'review_date': 'Review Date',
#        }
#        help_texts = {
#            'rating': 'Rate the console on a scale from 1 to 10.',
#            'review_date': 'Select the date of the review.',
#        }
#        error_messages = {
#            'rating': {
#                'invalid': 'Enter a valid rating between 1 and 10.',
#                'max_value': 'Rating cannot be more than 10.',
#                'min_value': 'Rating cannot be less than 1.',
#            },
#            'reviewer_name': {
#                'max_length': 'The reviewer name is too long.',
#            },
#        }
