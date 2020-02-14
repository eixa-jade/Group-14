"""
Definition of forms.
"""

from django import forms
from .models import Vendor
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = [
            'vendor_id', 
            'vendor_name', 
            'vendor_phone_number',
            'vendor_address',
            'vendor_email',
            ]