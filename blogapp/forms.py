from django import forms


class CommentForm(forms.Form):
    comment = forms.CharField(label="Comment", max_length=500, widget=forms.TextInput(attrs={'class':'commentbox', "placeholder":"Add new comment..."}))
