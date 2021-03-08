from django import forms
from questionyourmentor.models import Query

class QueryFormWithAttachment(forms.ModelForm):
    class Meta:
        model = Query
        fields = ('user', 'mentor_user_id', 'query_message', 'attachment', )

class QueryFormWithoutAttachment(forms.ModelForm):
    class Meta:
        model = Query
        fields = ('user', 'mentor_user_id', 'query_message', )

class QueryRespondForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ('response_message', )