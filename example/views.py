from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from django.views import View


class FirstView(View):

    def get(self, request):
        return HttpResponse('first')


class SecondView(View):

    def get(self, request):
        return HttpResponse('second')


class ThirdView(View):

    def get(self, request):
        return HttpResponse('third')


class AboutView(View):

    def get(self, request):
        return render(request, 'about.html')


class WelcomeView(View):

    def get(self, request):
        weeks = 15
        course = "Flask"
        group = "A 0101"

        context = {
            "weeks": weeks,
            "course": course,
            "group": group,
        }

        return render(request, 'welcome.html', context=context)


class StudentView(View):

    def get(self, request, student_id):


        students = {
            1: "Смирнов Хольгер Филиппович",
            2: "Демидович Налина Кирилловна",
            3: "Рыбакова Хитер Валерьевна",
            4: "Жуков Орион Святославович"
        }

        if student_id not in students:
            raise Http404

        context = {
            'student': students[student_id]
        }
        return render(request, 'student.html', context=context)
