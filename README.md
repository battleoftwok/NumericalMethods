# NumericalMethods
## Численные методы
Основные идеи:
1. Минимум внешних модулей, без внешних модулей для численных методов
1. Максимум комментариев в коде
1. Максимум русского языка
### Инструкция
#### Для запуска
1. Установить интерпретатор Python 3 и выше, который можно скачать с [официального сайта](https://www.python.org/downloads/)
1. Импортировать модуль main из папки code \
Например:
```python
from python_code.main import *
mat1 = Matrix([[20, 4, -8], [-3, 15, 5], [6, 3, -18]]) # Матрица из задания
free_column = [1, -2, 3] # Столбец свободных членов
print(solve(mat1, free_column, print_middle_values=True)) # Решит СЛАУ оптимальным способом и покажет пояснения
```
Для тех, кто совсем не понял, в корень репозитория добавлены файлы с названием "task%.py" просто подставьте числа из своего варианта.\
(Используйте только для самопроверки)\
Запуск программы (при установленном [интерпретаторе](https://www.python.org/downloads/)) - двойной левый клик мыши,
редактирование - правый клик мыши -> изменить
#### Для участия
1. Зарегистрироваться на [GitHub](http://github.com)
1. Написать свою почту (по которой регистрировался) в [личку](https://vk.com/simens_green) чтобы я добавил к разработчикам.
1. Если решил влезть в код, то рекомендую это делать с помощью [PyCharm](https://www.jetbrains.com/ru-ru/pycharm/) или 
([SublimeText3](https://www.sublimetext.com/3) или [Spyder](https://www.spyder-ide.org/) или [Atom](https://atom.io/)) + 
[Kite](https://www.kite.com/)
1. Для более удобного использования GitHub лучше установить [Git](https://ru.wikipedia.org/wiki/Git#:~:text=Git%20(%D0%BF%D1%80%D0%BE%D0%B8%D0%B7%D0%BD%D0%BE%D1%81%D0%B8%D1%82%D1%81%D1%8F%20%C2%AB%D0%B3%D0%B8%D1%82%C2%BB),%D0%B4%D0%B5%D0%BD%D1%8C%20%D0%B5%D0%B3%D0%BE%20%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%B8%D0%B2%D0%B0%D0%B5%D1%82%20%D0%94%D0%B6%D1%83%D0%BD%D0%B8%D0%BE%20%D0%A5%D0%B0%D0%BC%D0%B0%D0%BD%D0%BE.)-клиент, например сам 
[Git](https://git-scm.com/downloads) или [SublimeMerge](https://www.sublimemerge.com/) или [Github Desktop](https://desktop.github.com/)
### Структура
1. В папке [python_code](https://github.com/simensgreen/NumericalMethods/tree/master/python_code) 
лежит основной код программы (в случае желания редактировать - в _master_ **не пушить**!)
1. В папке [block diagrams](https://github.com/simensgreen/NumericalMethods/tree/master/block%20diagrams) должны лежать 
картинки с блок-схемами алгоритмов.
1. В папке [text descriptions](https://github.com/simensgreen/NumericalMethods/tree/master/text%20descriptions) должны 
лежать текстовые описания алгоритмов. \
P.S. в каждой папке по две папки - для разделения матриц и интергалов. В будущем структура может быть изменена.
