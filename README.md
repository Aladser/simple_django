# Склад

#### Заполнение БД
  * *data.json* - общий дамп таблиц
  * команда ``seed`` - сидирование из данных класса команды
  * команда ``seed_json`` - сидирование из дампа data.json

#### Модели
+ ``Category`` (*catalog/models/category.py*) - категория
+ ``Product`` (*catalog/models/product.py*) - товар
+ ``Contact`` (*catalog/models/contact.py*) - контакт

#### Контроллеры
+ ``products`` (*catalog/views/products/views.py*) - товар: index, show, create, store
+ ``contacts`` (*catalog/views.py*) - контакт

#### Шаблоны
+ *catalog/basic.html* - базовый шаблон
+ *catalog/product/[create.html, index.html, detail.html]* - страницы создания товара, списка товаров, отдельного товара
+ *catalog/contacts* - контакты
+ *catalog/components* - папка подшаблонов
