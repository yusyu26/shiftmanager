from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['date', 'starttime', 'endtime', 'author']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'starttime': forms.TimeInput(attrs={
                'type': 'time', 'step': '600',
                'class': 'form-control'
            }),
            'endtime': forms.TimeInput(attrs={
                'type': 'time', 'step': '600',
                'class': 'form-control'
            }),
            'author': forms.TextInput(attrs={
                'placeholder': '申請者名を入力してください',
                'class': 'form-control'
            }),
        }
        labels = {
            'date': '日付',
            'starttime': '開始時間',
            'endtime': '終了時間',
            'author': '申請者',
        }
