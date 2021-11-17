from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        # define model and fields to include
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # override init method to make changes to fields
        super().__init__(*args, **kwargs)
        # get all the categories
        categories = Category.objects.all()
        # create list of tuples with list comprehension to create for loop to add items to list
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # update category field to use friendly names instead of id - show in select box on form
        self.fields['category'].choices = friendly_names
        # iterate through rest of fields and add classes to match theme of store
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
