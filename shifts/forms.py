from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['date', 'starttime', 'endtime', 'author']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'starttime': forms.TimeInput(attrs={'type': 'time', 'step': '600'}),  # 10分間隔
            'endtime': forms.TimeInput(attrs={'type': 'time', 'step': '600'}),  # 10分間隔
            'author': forms.TextInput(attrs={'placeholder': '申請者名を入力してください'}),
            'substitute': forms.TextInput(attrs={'placeholder': '交代者名を入力してください'}),
        }
        labels =  {            
            'date': '日付',
            'starttime': '開始時間',
            'endtime': '終了時間',
            'author': '申請者',
            'substitute': 'シフト交代希望者',
            
        }

