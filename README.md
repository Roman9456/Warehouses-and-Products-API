# Warehouses-and-Products-API
# Overview
This project implements a REST API using Django Rest Framework (DRF) for managing products and warehouses. The API supports full CRUD operations (Create, Read, Update, Delete) for both products and warehouses, and includes search functionality and pagination.

# Description
The company manages various products stored in multiple warehouses. Each product is defined by its name and an optional description. Warehouses store these products and maintain specific storage costs for each product. Since a product may be stored in multiple warehouses, the storage cost can vary from warehouse to warehouse.

# Key Features
CRUD Operations:

Products: Create, retrieve, update, and delete product records.
Warehouses: Create, retrieve, update, and delete warehouse records.
Product-Warehouse Relationship:

Manage the association between products and warehouses, including specific storage costs.
Search Functionality:

Products: Search by name or description.
Warehouses: Search by the products they store, using either product ID or keywords in the product name/description.
Pagination: Implemented for product and warehouse lists to handle large datasets efficiently.

API Endpoints
Product Endpoints
Create Product: POST /products/

Request Body:
{
  "name": "Tomato",
  "description": "Fresh organic tomatoes"
}
Update Product: PATCH /products/{id}/

Request Body:
{
  "name": "Tomato",
  "description": "Updated description"
}
List Products: GET /products/

Response: A paginated list of products.
Retrieve Product: GET /products/{id}/

Response: Details of a single product by ID.
Delete Product: DELETE /products/{id}/

Warehouse Endpoints
Create Warehouse: POST /warehouses/

Request Body:
{
  "name": "Main Warehouse"
}
Update Warehouse: PATCH /warehouses/{id}/

Request Body:
{
  "name": "Main Warehouse"
}
List Warehouses: GET /warehouses/

Response: A paginated list of warehouses.
Retrieve Warehouse: GET /warehouses/{id}/

Response: Details of a single warehouse by ID, including stored products and their storage costs.
Delete Warehouse: DELETE /warehouses/{id}/

Search Endpoints
Search Products: GET /products/?search={keyword}

Example: GET /products/?search=Tomato
Search Warehouses by Product: GET /warehouses/?search={keyword}

Example: GET /warehouses/?search=Tomato# Склады и товары

## Техническая задача: реализовать CRUD-логику для продуктов и складов, используя Django Rest Framework.

**CRUD** — аббревиатура для Create-Read-Update-Delete. Ей обозначают логику для операций создания-чтения-обновления-удаления сущностей. Подробнее: https://ru.wikipedia.org/wiki/CRUD.

## Описание

У нас есть продукты, которыми торгует компания. Продукты описываются названием и необязательным описанием (см. `models.py`). Также компания имеет ряд складов, на которых эти продукты хранятся. У продукта на складе есть стоимость хранения, поэтому один и тот же продукт может иметь разные стоимости на разных складах.

Необходимо реализовать REST API для создания, получения, обновления, удаления продуктов и складов. Так как склады имеют информацию о своих продуктах через связанную таблицу, необходимо переопределить методы создания и обновления объектов в сериализаторе (см. `serializers.py`).

Помимо CRUD-операций, необходимо реализовать поиск продуктов по названиям и описанию. И поиск складов, в которых есть определенный продукт, по идентификатору. Подробности в файле `requests-examples.http`.

Так как продуктов и складов может быть много, то необходимо реализовать пагинацию для вывода списков.

Рекомендуется обратить внимание на реализацию файлов `urls.py`. Менять их не надо, просто обратить внимание и осознать.

## Подсказки

1. Вам необходимо будет задать логику во views и serializers. В места, где нужно добавлять код, включены комментарии. После того, как вы добавите код, комментарии можно удалить.

2. Для обновления объектов удобно использовать метод `update_or_create`: https://docs.djangoproject.com/en/3.2/ref/models/querysets/#update-or-create.

## Дополнительное задание

### Поиск складов с продуктами

Реализуйте поиск складов, в которых есть определённый продукт, но при этом указывать хочется не идентификатор продукта, а название, его часть или часть описания.

Пример запроса:

```
# поиск складов, где есть определенный продукт
GET {{baseUrl}}/stocks/?search=помид
Content-Type: application/json
```

## Документация по проекту

Для запуска проекта необходимо

Установить зависимости:

```bash
pip install -r requirements.txt
```

Вам необходимо будет создать базу в postgres и прогнать миграции:

```base
manage.py migrate
```

Выполнить команду:

```bash
python manage.py runserver
```
