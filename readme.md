Эксперимент по валидации json c использованием jsonschema

Схемы добавляются в список для проверки в случае корректности их структуры. 
Каждый json проверяется на соответствие всем корректным схемам и если проходит хотя бы 
одну валидацию - считается валидным. 

В файл сохраняется список невалидных JSON с ошибками валидации для каждой схемы.

каталоги исходных данных: 

    /task_folder/event - json
    /task_folder/schema - схемы

    
результат: 

    /results.txt
