Задание на практику от Estesis.tech

Образ с докерхаба
```
docker pull gimeori/couriers
```
```
docker run -p 7344:8000 --name test_courier firstimage
```

Приложение развернуто с помощью сервиса render.com
```
https://couriers-service.onrender.com/docs
```

<h1>Описание эндпоинтов</h1>


| method        | route             | description                                     |
|:------------- |:-----------------:| -----------------------------------------------:|
| POST          | /courier          | Регистрация курьера в системе                   |
| GET           | /couriers         | Получение списка всех курьеров                  |
| GET           | /courier/{id}     | Получение подробной информации о курьере по id  |
| POST          | /order            | Публикация заказа в системе                     |
| GET           | /order/{id}       | Получение информации о заказе                   |
| POST          | /order/{id}       | Завершение заказа                               |
| GET           | /docs             | Документация API                                |


