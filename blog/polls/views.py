from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice_selected = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Question.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': Question,
            'error_message': "You didn't select a choice."
        })
    else:
        choice_selected.votes += 1
        choice_selected.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question_id, )))


