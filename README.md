# vuz
## Программа для поиска ВУЗов на основе среднего балла по шокльным предметам
__Внимание__, результаты, даваемые программой не претендуют на точность, они носят не рекомендательный, а лишь ознакомительный характер
## Обзор подпрограмм
|||
|-|-|
|`rsr.py` | Поисковик олимпиад, с него и начался этот проект. При запуске без параметров, выводит все известные олимпиады. Также можно запускать `./rsr.py название_предмета` или `./rsr.py III` - для поиска олимпиад третьего уровня, `./rsr.py --update` - обновление локальной базы данных (получение свежего списка олимпиад). Пример: `./rsr.py информ I` выводит все олимпиады по информатике первого уровня| 
|`grades.py`| Перевод из псевдо-xls в csv: `./grades.py --update`|
|`vuz.py`| Основная программа, которая объединяет предыдущие две и добавляет свой функционал - поиск вузов онлайн|  
|`marks.py`| Считает, сколько оценок вам нужно получить, чтобы средний балл по предмету стал 4,5. После запуска необходимо ввести через пробел все оценки по предмету. Программа автоматически посчитает количество оценок, средний балл и недостающее число пятёрок и т.д.  Также высчитывает количество оценок "2", "3" или "4" после которого балл упадёт ниже 4,5 |  
|`adv.py`| Продвинутый поисковик олимпиад, выводит предстоящие олимпиады и их даты: `./adv.py информ I`|
## Как это работает?
Всё, что от вас требуется - это поместить ваши оценки в таблицу .csv  
Есть два способа сделать это:
- Так как это муторный процесс, можно воспользоваться утилитой `grades.py`, которая переведёт таблицу с оценками из формата .xls (не путать с .xslx) в .csv.  
__Важно!__ Программа разрабатывалась под электронный дневник именно моей школы, поэтому, на данном этапе есть свои особенности. Так, файл .xls на самом деле не таблица Excel (который по меньшей мере должен предсавлять из себя zip-архив), а обычная HTML-таблица. Поэтому перевод xls -> csv происходит с помощью парсера BeautifulSoup и стандартного модуля csv.
- _Если вы создаёте таблицу самостоятельно,_ то достаточно двух столбцов: название предмета и средний балл - __программа берёт уже готовый средний балл, а не считает его сама!__ - учитывайте это, если вы любитель редактировать файлы всяких программ.  

Итак, имеем файл grades.csv  
В самом начале работы программы, ползователь указал предметы, которые хочет сдавать на ЕГЭ.
Теперь нам нужно взять из таблицы средние баллы по указанным предметам и предположить, какими будут результаты ЕГЭ.
Вот как это делается. Самому низкому среднему баллу (2.0) присваивается самый низкий теоретически возможный балл ЕГЭ - 0, самому высокому ср. баллу по пятибальной шкале (5.0) - наивысший б. ЕГЭ - 100:
|Средний балл по предмету|Предпологаемый балл за ЕГЭ по предмету|
|-|-|
| 2.0 | 0 |
|...|...|
|5.0| 100 |   

Таким образом, можно расчитать (обобщённо и неточно) какие баллы по ЕГЭ может получить ученик.  
Теперь остаётся лишь выполнить поиск вуза в нужном городе с заданными баллами ЕГЭ. Для этого посылается запрос на сайт vuzopedia.ru, откуда мы получаем список вузов, который и выводится пользователю.  
Также, если пользователь указал это, программа может вывести список олимпиад по сдаваемым предметам ЕГЭ, однако предпологаемый балл за экзамен должен быть не менее 75. Конечно же, вы можете просто выполнить поиск олимпиад на сайте rsr-olymp.ru с помощью `rsr.py`
