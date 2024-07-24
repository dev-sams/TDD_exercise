import random
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404

from xword_data.models import Clue
# Create your views here.


class DrillView(View):
    template_name = 'xword_data/drill.html'

    def get(self, request):
        clues = Clue.objects.all()
        clue = random.choice(clues)
        return render(request, self.template_name, {'clue': clue})

    def post(self, request):
        clue_id = request.POST.get('clue_id')
        clue = get_object_or_404(Clue, id=clue_id)
        user_guess = request.POST.get("guess", "").upper()
        related_clues = Clue.objects.filter(entry=clue.entry).exclude(id=clue.id)
        if user_guess == clue.entry.entry_text.upper():
            return redirect(reverse('xword-answer', kwargs={'clue_id': clue.id}))
        else:
            return render(request, self.template_name, {
                'clue': clue,
                'error': 'Answer is incorrect. Try again!'
            })


class DrillAnswerView(TemplateView):
    template_name = 'xword_data/answer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clue_id = kwargs.get('clue_id')
        clue = get_object_or_404(Clue, id=clue_id)
        related_clues = Clue.objects.filter(clue_text=clue.clue_text)
        context['clue'] = clue
        context['related_clues'] = related_clues
        return context
