# В пакете coxtext размещаются функции для расширения шаблона
# Необходимо прописать функции в settings.py TEMPLATES

import datetime

def year(request):                          # для футера
    year = datetime.datetime.now().year
    return {'year': year}
