
from django import forms
from .models import Contact, Order


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-4 bg-[#3a1f0e] border border-[#f2b84b]/30 rounded-xl text-white placeholder-[#c7b29a] focus:outline-none focus:border-[#f2b84b] focus:ring-2 focus:ring-[#f2b84b]/30 transition',
                'placeholder': 'Enter your full name',
                'required': 'required',
                'autocomplete': 'name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-4 bg-[#3a1f0e] border border-[#f2b84b]/30 rounded-xl text-white placeholder-[#c7b29a] focus:outline-none focus:border-[#f2b84b] focus:ring-2 focus:ring-[#f2b84b]/30 transition',
                'placeholder': 'your.email@example.com',
                'required': 'required',
                'autocomplete': 'email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full p-4 bg-[#3a1f0e] border border-[#f2b84b]/30 rounded-xl text-white placeholder-[#c7b29a] focus:outline-none focus:border-[#f2b84b] focus:ring-2 focus:ring-[#f2b84b]/30 transition',
                'placeholder': 'How can we help you today?...',
                'rows': 6,
                'required': 'required'
            }),
        }

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message and len(message.strip()) < 10:
            raise forms.ValidationError("Message must be at least 10 characters long.")
        return message


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={
                'class': 'w-20 p-3 bg-[#3a1f0e] border border-[#f2b84b]/30 rounded-xl text-white text-center focus:outline-none focus:border-[#f2b84b]',
                'min': '1',
                'value': '1',
                'required': 'required'
            }),
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity < 1:
            raise forms.ValidationError("Quantity must be at least 1.")
        return quantity