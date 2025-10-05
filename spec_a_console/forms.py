from django import forms
from .models import ConsoleSystem
from .models import SystemReview


# class SpecAConsoleForm(forms.ModelForm):
#     class Meta:
#         model = SpecAConsole
#         fields = [
#             'name',
#             'description',
#             'release_date',
#             'manufacturer',
#             'price',
#             'specifications',
#         ]
#         widgets = {
#             'release_date': forms.DateInput(attrs={'type': 'date'}),
#             'description': forms.Textarea(attrs={'rows': 4}),
#             'specifications': forms.Textarea(attrs={'rows': 4}),
#         }
#         labels = {
#             'name': 'Console Name',
#             'description': 'Brief Description',
#             'release_date': 'Release Date',
#             'manufacturer': 'Manufacturer',
#             'price': 'Launch Price (USD)',
#             'specifications': 'Technical Specifications',
#         }
#         help_texts = {
#             'price': 'Enter the launch price in USD.',
#             'release_date': 'Select the release date of the console.',
#         }
#         error_messages = {
#             'name': {
#                 'max_length': 'The name is too long.',
#                 'unique': 'A console with this name already exists.',
#             },
#             'price': {
#                 'invalid': 'Enter a valid price.',
#             },
#         }


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
