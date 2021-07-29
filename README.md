# Документация по API
## 1. Функционал для администратора системы
### 1.1 Авторизация в системе

  POST /auth/token/login/
    
    Тело запроса содержит имя пользователя и пароль:
    username=admin
    password=admin
    
    Тело ответа:
    {
      "auth_token": "token_admin"
    }
    
Пример:

    
  ![1](https://user-images.githubusercontent.com/64875702/127546879-8fee9bd1-2568-43f0-9165-fb1df8a389a4.PNG)
 
### 1.2 Выход из системы

POST /auth/token/logout/

В `headers` необходимо передать содержимое:

`Authorization: Token token_admin`

`Content-Type: application/json`

### 1.3 Просмотр созданных опросов

GET /api/admin/surveys

В `headers` необходимо передать содержимое:

`Authorization: Token token_admin`

`Content-Type: application/json`

Тело ответа:

    {
        "surveys": [
            {
                "name": "Название вопроса",
                "start_date": "Дата старта в формате YYYY-MM-DD",
                "end_date": "Дата окончания в формате YYYY-MM-DD",
                "description": "Описание опроса",
                "questions": #Список вопросов в опросе
                [
                    {
                        "title": "Название вопроса",
                        "type": Тип вопроса(int) 1,2, или 3
                        "true_answer_text": "Верный ответ для вопроса типа 1"
                        "list_answer_text": [ # Список с вариантами ответов для вопроса типа 2 или 3. Для типа 1 список пуст
                            {
                                "title": "Название варианта ответов"
                            },
                            {
                             ...
                            }
                        ],
                        "choice_answers_line": "№ верного варианта ответа, начиная с 1. Если ответов несколько - ответы разделять ; ",
                        "id": id вопроса(int) 
                    }
                ],
                "id": id опроса(int)
            },
            {
            ...
            }
            ]
     }

Пример

![2](https://user-images.githubusercontent.com/64875702/127551411-3463d9d5-c77c-4c0e-8af1-9de26d97ae4f.PNG)

### 1.4 Редактирование созданных опросов

При редактировании опросов также можно можно редактировать вопросы, находящиеся в опросе

PUT /api/admin/surveys/{id}

`id`- id редактируемого опроса


В `headers` необходимо передать содержимое:

`Authorization: Token token_admin`

`Content-Type: application/json`

Тело запроса:

    {
        "surveys": [
            {
                "name": "Название вопроса",
                "end_date": "Дата окончания в формате YYYY-MM-DD",
                "description": "Описание опроса",
                "questions": #Список вопросов в опросе
                [
                    {
                        "title": "Название вопроса",
                        "type": Тип вопроса(int) 1,2, или 3
                        "true_answer_text": "Верный ответ для вопроса типа 1"
                        "list_answer_text": [ # Список с вариантами ответов для вопроса типа 2 или 3. Для типа 1 список пуст
                            {
                                "title": "Название варианта ответов"
                            },
                            {
                             ...
                            }
                        ],
                        "choice_answers_line": "№ верного варианта ответа, начиная с 1. Если ответов несколько - ответы разделять ; ",
                        "id": id вопроса(int) 
                    }
                ],
                "id": id опроса(int)
            },
            {
            ...
            }
            ]
     }

### 1.5 Удаление созданных опросов

DELETE /api/admin/surveys/{id}

`{id}`- id удаляемого опроса

В `headers` необходимо передать содержимое:

`Authorization: Token token_admin`

`Content-Type: application/json`



### 1.6 Просмотр созданных вопросов

GET /api/admin/questions

В `headers` необходимо передать содержимое:

`Authorization: Token token_admin`

`Content-Type: application/json`

Тело ответа:

    {
        "questions": [ #Список созданных вопросов
            {
                    "title": "Название вопроса",
                    "type": Тип вопроса(int) 1,2, или 3
                    "true_answer_text": "Верный ответ для вопроса типа 1"
                    "list_answer_text": [ # Список с вариантами ответов для вопроса типа 2 или 3. Для типа 1 список пуст
                        {
                            "title": "Название варианта ответов"
                        },
                        {
                         ...
                        }
                    ],
                    "choice_answers_line": "№ верного варианта ответа, начиная с 1. Если ответов несколько - ответы разделять ; ",
                    "id": id вопроса(int) 
                },
            
            {
            ...
            }
            ]
    }
    
    
### 1.7 Редактирование созданных вопросов

PUT /api/admin/questions/{id}

`id`- id редактируемого вопроса


В `headers` необходимо передать содержимое:

`Authorization: Token token_admin`

`Content-Type: application/json`

Тело запроса

    {
        "question": 
            {
                 "title": "Название вопроса",
                    "type": Тип вопроса(int) 1,2, или 3
                    "true_answer_text": "Верный ответ для вопроса типа 1"
                    "list_answer_text": [ # Список с вариантами ответов для вопроса типа 2 или 3. Для типа 1 список пуст
                        {
                            "title": "Название варианта ответов"
                        },
                        {
                         ...
                        }
                    ],
                    "choice_answers_line": "№ верного варианта ответа, начиная с 1. Если ответов несколько - ответы разделять ; ",
                    
               
            }     
    }
    
### 1.8 Удаление созданных вопросов

DELETE /api/admin/questions/{id}

`id`- id удаляемого вопроса

В `headers` необходимо передать содержимое:

`Authorization: Token token_admin`

`Content-Type: application/json`








  
