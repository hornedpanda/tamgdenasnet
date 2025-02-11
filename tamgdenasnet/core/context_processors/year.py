import datetime


def year(request):
    """Добавляет переменную с текущим годом."""
    cur_date = datetime.datetime.now()
    return {
        'year_now': cur_date.year,
    }


# def font_color(koef):
#     if koef > 75:
#         return f"<font color = 'blue'>{koef}%</font>"
#     else:
#         return koef