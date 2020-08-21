from django import forms
from .models import Artist, gallery1,artist_work

class AddArtist_Form(forms.ModelForm):

    class Meta:
        model = Artist
        fields = ['a_name', 'a_img', 'a_contact', 'a_email', 'a_des', 'a_fb', 'a_insta']

class Addimggal1_Form(forms.ModelForm):

    class Meta:
        model = gallery1
        fields = ['g1_img']


class AddWork_form(forms.ModelForm):
    class Meta:
        model = artist_work
        fields = ['a_id', 'w_img']

