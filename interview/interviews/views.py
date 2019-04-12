from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView
from .models import User, Quiz, Question
from .questions import QUESTIONS

from django.forms import ModelForm


class BeginForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class QuestionForm(ModelForm):

    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       # make the question field read-only
       self.fields['question'].widget.attrs['readonly'] = True

    class Meta:
        model = Question
        fields = ('question', 'answer')


def begin_view(request):
    """View function for kicking off
    an data science challenge.
    """
    if request.method == 'POST':
        # create a form instance with the submitted data
        form = BeginForm(request.POST)
        # validate the form
        if form.is_valid():
            # create and save user object
            user = form.save()
            # create and save quiz object
            quiz = Quiz(user=user)
            quiz.save()
            # add the questions
            for question in QUESTIONS:
                # create question object and link it
                q = Question(quiz=quiz, **question)
                q.save()
            # redirect to the quiz view
            return redirect('/quiz/{}/'.format(quiz.id))
    else:
        form = BeginForm()

    return render(request, 'interviews/start.html', {'form': form})


def question_view(request, pk):
    """View function for looping through
    a quizzes questions.
    """
    # get quiz and questions
    quiz = Quiz.objects.filter(id=pk).first()
    question = quiz.question_set.filter(answer=None).first()
    # if no question, redirect to beginning
    if question is None:
        redirect('/admin/')
    if request.method == 'POST':
        # use POST data to update question object
        form = QuestionForm(request.POST, instance=question)
        # validate form
        if form.is_valid():
            question = form.save()
            return redirect('/quiz/{}/'.format(quiz.id))
    else:  # 5
        # Create an empty form instance
        form = QuestionForm(instance=question)

    return render(request, 'interviews/quiz.html', {'form': form})
