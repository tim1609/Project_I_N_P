from django.shortcuts import render

title = 'Тортуга Нашего времени'



def index(request):
    context = {'title': title,
               'text': 'Главная Страница',
               "names":["Рома", "Коля", "Вася", "Петя", "Маша"],
               'Content1': '[Рымник.] Сдѣлалъ верхомъ переходъ до Рымника. [[5]] Старикъ все не кланяется мнѣ. Обѣ вещи эти злятъ меня. Съ встрѣчавшимися баши-бузуками велъ себя хорошо. Объяснился съ Крыжановскимъ. Онъ, не знаю зачѣмъ, совѣтуетъ мнѣ прикомандироватьсякъ казачьей батареѣ; совѣтъ, которому я не послѣдую. Желчно спорилъ вечеромъ съ Фридеи Бабарыкинымъ, ругалъ Сержпутовскому и ничего не сдѣлалъ, вотъ 3 упрека, которыя дѣлаю с ебѣ за нынѣшній день. (3) '}
    template = 'posts/index.html'
    return render(request, template, context)

def group_posts(request):
    template = 'posts/group_list.html'
    return render(request, template)


