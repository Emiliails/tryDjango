# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# use shortcuts
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

# use generic views
# ListView: display a list of objects
class IndexView(generic.ListView):
    # Similarly, the ListView generic view uses a default template called <app name>/<model name>_list.html
    # we use template_name to tell ListView to use our existing "polls/index.html" template.
    template_name = 'polls/index.html'
    # However, for ListView, the automatically generated context variable is question_list.
    # To override this we provide the context_object_name attribute,
    # specifying that we want to use latest_question_list instead.
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


# def detail(request, question_id):
#     return HttpResponse("You're looking at the results of questions %s." % question_id)

# handle exception
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})

# use shortcuts
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# use generic views
# DetailView: display a detail page for a particular type of object
class DetailView(generic.DetailView):
    # Each generic view needs to know what model it will be acting upon. This is provided using the model attribute.
    model = Question
    # By default, the DetailView generic view uses a template called <app name>/<model name>_detail.html.
    # In our case, it would use the template "polls/question_detail.html".
    # The template_name attribute is used to tell Django to use a specific template name
    # instead of the autogenerated default template name.
    template_name = 'polls/detail.html'
    # In previous parts of the tutorial,
    # the templates have been provided with a context
    # that contains the question and latest_question_list context variables.
    # For DetailView the question variable is provided automatically –
    # since we’re using a Django model (Question),
    # Django is able to determine an appropriate name for the context variable.


# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html',
                      {'question': question, 'error_message': "You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# use shortcuts
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

# use generic view
class ResultsView(generic.DetailView):
    model = Question
    # We also specify the template_name for the results list view –
    # this ensures that the results view and the detail view have a different appearance when rendered,
    # even though they’re both a DetailView behind the scenes.
    template_name = 'polls/results.html'
