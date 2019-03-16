from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.utils import timezone

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {'latest_question_list': latest_question_list}
    return render(request, 'questions/index.html', context)


@require_POST
def add_question(request):
    new_question = Question(question_text=request.POST.get("question", ""),
                            pub_date=timezone.now())
    new_question.save()

    return redirect('/questions')
