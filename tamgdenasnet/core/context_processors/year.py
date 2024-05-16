import datetime
def year(request):
    """Добавляет переменную с текущим годом."""
    cur_date = datetime.datetime.now()
    return {
        'year_now': cur_date.year,
    }