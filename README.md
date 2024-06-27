# Склад

#### Заполнение БД
  * *data.json* - общий дамп таблиц
  * команда ``seed`` - сидирование из данных класса команды
  * команда ``seed_json`` - сидирование из дампа data.json

#### Модели
+ ``Category`` (*catalog/models/category*) - категория
+ ``Product`` (*catalog/models/product*) - товар
+ ``Contact`` (*catalog/models/contact*) - контакт

#### Контроллеры
+ ``products`` (*catalog/views/products*) - товар: index, show, create, store
+ ``contacts`` (*catalog/views/contacts*) - контакт

#### Шаблоны
+ *catalog/basic.html* - базовый шаблон
+ *catalog/product/[create.html, index.html, detail.html]* - страницы создания товара, списка товаров, отдельного товара
+ *catalog/contacts* - контакты
+ *components* - папка подшаблонов