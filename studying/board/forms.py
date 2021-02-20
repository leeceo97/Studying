from django import forms
from .models import Comment

class BoardForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required': '제목을 입력해주세요.'
        },
        max_length=128, label="제목")
    contents = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요.'
        },
        widget=forms.Textarea, label="내용")
    image = forms.ImageField(
        error_messages={
            'required': '이미지를 넣어주세요.'
        },
        label="이미지"
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('body',)