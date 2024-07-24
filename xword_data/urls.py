from django.urls import path
from xword_data.views import DrillView, DrillAnswerView

urlpatterns = [
    path('', DrillView.as_view(), name="xword-drill"),
    path('drill_answer/<int:clue_id>/', DrillAnswerView.as_view(), name="xword-answer"),
]