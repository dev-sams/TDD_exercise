from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
import random

from xword_data.models import Clue

class DrillView(View):
    template_name = 'drill.html'

    def get(self, request):
        clues = Clue.objects.all()
        clue = random.choice(clues)
        return render(request, self.template_name, {'clue': clues, 'clue_id': clues.id})

    def post(self, request):
        clue_id = request.POST.get('clue_id')
        clue = get_object_or_404(Clue, id=clue_id)
        user_guess = request.POST.get("answer", "").upper()
        if user_guess == clue.entry.entry_text.upper():
            # Store a success message in the session and redirect to the answer view
            request.session['message'] = f'{clue.entry.entry_text.upper()} is the correct answer! You have now answered 1 (of 3) clues correctly'
            return redirect(reverse('xword-answer', kwargs={'clue_id': clue.id}))
        else:
            # Return an error message if the answer is incorrect
            return render(request, self.template_name, {
                'clue': clue,
                'clue_id': clue.id,
                'error': 'Answer is not correct. Try again!'
            })

class DrillAnswerView(TemplateView):
    template_name = 'answer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clue_id = kwargs.get('clue_id')
        clue = get_object_or_404(Clue, id=clue_id)
        related_clues = Clue.objects.filter(clue_text=clue.clue_text)
        related_entries_count = related_clues.values('entry__entry_text').annotate(count=models.Count('entry__entry_text')).order_by('-count')
        context['clue'] = clue
        context['related_clues'] = {item['entry__entry_text']: item['count'] for item in related_entries_count}
        # Retrieve the success message from the session
        context['message'] = self.request.session.pop('message', None)
        return context
