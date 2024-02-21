from django import forms
from user.models import User

class ProfileForm(forms,ModelForm):
    class Meta:
        model = Profile
        fields = [
            'dating_sex','location','min_distance',
            'max_distance','min_dating_age','max_dating_age',
            'vibration','only_matche','auto_play'
        ]

    def clean_min_dating_age(self):
        cleaned_date = super().clean()
        min_dating_age = cleaned_date['min_dating_age',0]
        max_dating_age = cleaned_date['max_dating_age',-1]
        if min_dating_age > max_dating_age:
            raise forms.ValidationError('min_dating_age > max_dating_age')