from django import forms

from Basic_exam.web.models import Profile, Album


class CreateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'user_name': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'age': forms.TextInput(attrs={'placeholder': 'Age'}),
        }


class DeleteProfile(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class AddAlbum(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'image': forms.TextInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.TextInput(attrs={'placeholder': 'Price'}),
        }


class EdieAlbum(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class DeleteAlbum(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, fild in self.fields.items():
            fild.widget.attrs['disabled'] = 'disabled'
            fild.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = '__all__'
