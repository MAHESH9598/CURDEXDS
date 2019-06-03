from django import forms
class InsertForm(forms.Form):
    product_id = forms.IntegerField(
        label='Enter product_id:',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'product Id'
            }
        )

    )
    product_name = forms.CharField(
        label='Enter Product Name:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product name'
            }
        )
    )
    product_cost = forms.IntegerField(
        label='Enter product cost:',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter cost'

            }
        )

    )
    product_color = forms.CharField(
        label='Enter product color:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter color'
            }
        )
    )
    product_class = forms.CharField(
        label='Enter Product Class:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Class'
            }
        )
    )
    customer_name = forms.CharField(
        label='Enter Customer Name:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter name'
            }
        )
    )
    customer_mobile = forms.IntegerField(
        label='Enter customer mobile:',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter mobile'
            }
        )
    )
    customer_email = forms.EmailField(
        label='Enter Customer Email:',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Email'
            }
        )
    )

class UpdateForm(forms.Form):
    product_id = forms.IntegerField(
        label='Enter Your Id:',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter id'
            }
        )
    )
    product_cost = forms.IntegerField(
        label='Enter product cost:',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter cost'

            }
        )

    )

class DeleteForm(forms.Form):
    product_id = forms.IntegerField(
        label='Enter product_id:',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product Id'
            }
        )

    )