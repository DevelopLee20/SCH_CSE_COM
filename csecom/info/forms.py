from .models import *
from calendar import HTMLCalendar
from django import forms
from django.urls import reverse


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()
    #Calendar객체 호출하고 super로 클래스를 초기화
 
    def formatday(self, day, contents):
        contents_day = contents.filter(start_time__day=day)
        d = ''
        for cont in contents_day:
            d += f'<li> {cont.content} </li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        
        return f'<td></td>'
    #{day} </a> <ul> {d} </ul></td>'

    #filter():데이터베이스 테이블의 열(col)과 연결된 모델을 호출
    #formatday함수는 달력에서 하루를 형식화하는 함수 모델 schedule의 events를 받아 출력

    def formatweek(self, week, contents):
        wk = ''
        for d, weekday in week:
            wk += self.formatday(d, contents)
        return f'<tr> {wk} </tr>'
    #formatweek함수는 달력에서 주를 형식화하는 함수

    def formatmonth(self, withyear=True):
        contents = schedule.objects.filter(start_time__year=self.year, start_time__month=self.month)
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        #formatmonth함수: 달력의 이름
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            #monthdays2calendar: 그 해에 맞춰진 날짜
            cal += f'{self.formatweek(week, contents)}\n'
        return cal
    
    #def formatweekheader(self):
    #    days = ['일', '월', '화', '수', '목', '금', '토']
    #    weekheader = ''.join(f'<th class="{self.cssclasses[weekday]}">{day}</th>' for weekday, day in enumerate(days))
    #    return f'<tr>{weekheader}</tr>'

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = schedule
        fields = ['content']
        labels = {
            'content': '일정',
        }

