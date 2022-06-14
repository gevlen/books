# books

## Запуск сервиса и произведение миграций
1. Для Windows
  - Через консоль из корня проекта 
  ```
  set FLASK_APP=app.py (возможно потребуется ввести)
  flask db upgrade
  flask run
  ```
  - Запустив ```app.py```
2. Для Linux
  - Через консоль из корня проекта 
  ```
  export FLASK_APP=app.py (возможно потребуется ввести)
  flask db upgrade
  flask run
  ```
  - Запустив ```app.py```

## Endpoints

- ```127.0.0.1:5000/api/books```

  GET - возвращает список всех книг и информацию по ним
  ```json
    [
    {
        "id": 1, # id книги
        "created_at": "2022-05-19", # дата создания в бд
        "updated_at": "2022-05-20", # дата обновления в бд
        "title": "nazvanieknigi1", # название книги
        "author": {
            "name": "authorname1", # имя автора
            "id": 1 # id автора
        }
    }
    ]
    ```
  
  POST - создает новую книгу:
    ```json
    {
    "title": "nazvanie knigi", # обязательный параметр
    "author_id": 1 # если не указать, то присвоит значение null
    }
    ```
    
- ```127.0.0.1:5000/api/books/<id>```

  GET - возвращает информацию по книге 
  ```json
    {
    "id": 1,
    "created_at": "2022-05-19",
    "updated_at": "2022-05-20",
    "title": "nazvanieknigi1",
    "author": {
        "name": "authorname1",
        "id": 1
    }
  }
    ```
  PUT - изменяет информацию по книге
  ```json
    {
    "title": "novoe nazvanie knigi", # иожно изменить назваеие, необязательный параметр
    "author_id": 2 # можно изменить автора, необязательный параметр
    }
    ```
    
  DELETE - удаляет книгу
  
- ```127.0.0.1:5000/api/authors```

  GET - возвращает список всех авторов и информацию по ним
  ```json
    [
    {
        "name": "authorname1", # имя автора
        "books": [
            {
                "title": "nazvanieknigi1", # название книги
                "id": 1 # id книги
            }
        ],
        "id": 1 # id автора
    }
  ]
    ```
  
  POST - создает нового автора:
    ```json
    {
    "name": "authorname2" # имя автора, id присваивается автоматически
    }
    ```
    
- ```127.0.0.1:5000/api/authors/<id>```

  GET - возвращает информацию про автора 
  ```json
   {
    "name": "authorname1", # имя автора
    "books": [
        {
            "title": "nazvanieknigi1", # название книги
            "id": 1 # id книги
        }
    ],
    "id": 1 # id книги
  }
    ```
  PUT - изменяет информацию про автора
  ```json
    {
    "name": "novoe nazvanie knigi" # иожно изменить имя автора
    }
    ```
    
  DELETE - удаляет автора
  
    если у автора были книги, то присвоит этим книгам "autor_id"=null 
    
