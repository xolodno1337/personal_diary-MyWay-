from django.forms import ModelForm
from diary.models import Diary


class DiaryUpdateForm(ModelForm):
    class Meta:
        model = Diary
        fields = ('title', 'image', 'context', 'date_event', 'is_active')
