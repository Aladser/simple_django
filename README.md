# Склад

#### Заполнение БД
  * *data.json* - общий дамп таблиц
  * команда ``seed`` - сидирование из данных класса команды
  * команда ``seed_json`` - сидирование из дампа data.json

#### Модели
+ ``Category`` - категория
+ ``Product`` - товар
+ ``Contact`` - контакт

#### Контроллеры
+ ``products`` (*catalog/views/products*) - товары: index, show, create, store
+ ``contacts`` (*catalog/views*) - контакты