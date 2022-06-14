# Sales (DRF)

Проект реализован в рамаках тестового задания, содержит фронтенд часть на React.

## Функционал

- получение данных из определенного листа Google Sheet по API 
- подсчёт цены заказа в рублях путем получения курса валюты по API Центрального Банка
- удаление/изменение данных в базе данных при удалении/изменении данных в Google Sheet

## В разработке применяется

- python 3.10
- docker
- docker-compose
- Django(DRF)

## Запуск

### Docker

```
git clone git@github.com:Kannykl/SalesDRF-2022.git
chmod +x entrypoint.sh
docker-compose up -d  --build
```

