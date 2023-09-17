# product-accounting-console-application
Консольное приложение на Python для учёта продуктов.

**Цель работы:**
Создать программное обеспечение системы обработки данных: «Программа для контроля собственных денежных средств».
Необходимо реализовать следующие функции, позволяющие:
1. Добавлять продукт в коллекцию (тип коллекции на ваш выбор).
2. Просматривать все записанное в программу.
3. Просматривать покупки по дате и категории.
4. Распределять их по стоимости от минимальной к максимальной или наоборот.
5. Удалять требуемые записи и выходить из программы.


**Описание работы**
Программа разделена на следующие классы: 
-	**Product** является объектом продукта. Содержит параметры id, name, price, category, date, где id и date генерируются автоматически
-	**Interpreter** является связующим звеном между приложением и консолью. Он просит ввести команду с клавиатуры, обрабатывает её и выполняет, если она существует.
-	**CommandManager** содержит все доступные команды для взаимодействия с коллекцией. Может зарегистрировать команду или выполнить её по имени.
-	**CollectionManager** хранит коллекцию и содержит всю основную логику по работе с ней. 


**Работа программы:**
1.	Выводятся приветственные слова
2.	Ожидается ввод команды
3.	Если команда существует (обращение к менеджеру команд), начинается выполнение команды
4.	Обращение к менеджеру коллекций (add, show и т. д.)
5.	Менеджер коллекций выполняет запрос команды и возвращает ответ (если он требуется)
6.	Если нужно, команда просит ввода с клавиатуры, и выводит результат работы
7.	Выполнение продолжается с пункта 2.


**Инстрункция по запуску:**
1. Убедитесь, что на компьютере установлен Python 3
2. Откройте "Запустить программу.bat"
