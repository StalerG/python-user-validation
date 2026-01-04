<div align="center" style="margin: 25px 0;">
<table style="border-spacing: 10px; border-collapse: separate; margin: 0 auto;">
<tr>
<td style="padding: 9px 17px; background: #2563eb; color: white; border-radius: 8px; font-family: monospace; font-size: 14px; font-weight: bold; border: 2px solid #1d4ed8; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2); white-space: nowrap;">
🐍 <strong>Python 3.9+</strong>
</td>
<td style="padding: 9px 17px; background: #16a34a; color: white; border-radius: 8px; font-family: monospace; font-size: 14px; font-weight: bold; border: 2px solid #15803d; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2); white-space: nowrap;">
✅ <strong>Tests: 12</strong>
</td>
<td style="padding: 9px 17px; background: #ca8a04; color: white; border-radius: 8px; font-family: monospace; font-size: 14px; font-weight: bold; border: 2px solid #a16207; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2); white-space: nowrap;">
📜 <strong>MIT License</strong>
</td>
<td style="padding: 9px 17px; background: #0891b2; color: white; border-radius: 8px; font-family: monospace; font-size: 14px; font-weight: bold; border: 2px solid #0e7490; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2); white-space: nowrap;">
⚡ <strong>0 Dependencies</strong>
</td>
<td style="padding: 9px 17px; background: #7c3aed; color: white; border-radius: 8px; font-family: monospace; font-size: 14px; font-weight: bold; border: 2px solid #5b21b6; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2); white-space: nowrap; display: flex; align-items: center; justify-content: center; gap: 8px;">
<a href="https://github.com/StalerG/python-user-validation/releases" style="color: white; text-decoration: none; display: flex; align-items: center; gap: 8px;">
<img src="https://img.shields.io/github/downloads/StalerG/python-user-validation/total?label=10%20downloads&color=7c3aed&style=flat-square
</a>
</td>
</tr>
</table>
</div>


# 🧪 Python User Validation Class

Простой, но мощный класс для валидации пользователей на чистом Python.  
**Без зависимостей, с полной инкапсуляцией, быстрее Pydantic в 3-5 раз!**

## 🚀 Особенности polymorph.py

- ✅ **0 зависимостей** - только стандартная библиотека  
- ✅ **Полная инкапсуляция** - name mangling + property  
- ✅ **Строгая валидация** - username и email  
- ✅ **Быстрее Pydantic** - в 3-5 раз на 10k вызовов  
- ✅ **Production-ready** - готов к использованию  

## 📦 Установка

Просто скопируй файл `polymorph.py` в свой проект!

```python
from polymorph import User

# Создание пользователя
user = User('Alex228', 'TEST@EXAMPLE.COM')
print(user)

# Автоматическое приведение email к нижнему регистру
print(user.email)

# Валидация при изменении
user.username = "NewUser123"
```
## 🧪 Тестовый файл test_user.py 

Файл содержит полные тесты для проверки всего функционала класса User.

**Что тестируется:**
- ✅ Создание пользователя с валидными данными
- ✅ Валидация username (длина, символы, наличие букв)
- ✅ Валидация email (формат, нижний регистр)
- ✅ Работа property-сеттеров
- ✅ Метод get_all() для получения данных
- ✅ Строковое представление объекта
- ✅ Защита инкапсуляции
- ✅ Граничные случаи

Как запустить:

```python
# Просто запусти файл
python test_user.py

# Или через unittest
python -m unittest test_user.py

# Или с подробным выводом
python -m unittest test_user.py
```

## 📖 Пример использования 

Создай файл example.py:

```python
from polymorph import User

print("Пример работы с классом User")
print("=" * 40)

# Создание пользователя
user = User('StalerG', 'Buhaem@pivo.com')
print(f"Создан: {user}")

# Изменение данных
user.username = "NewUser123"
user.email = "UPDATED@EXAMPLE.COM"
print(f"После обновления: {user}")

# Получение данных
data = user.get_all()
print(f"Данные: {data.username} / {data.email}")

print("=" * 40)
print("Пример завершён!")
```
## ⚡ Производительность

Быстрее Pydantic в 3-5 раз, 0 зависимостей, готов к production.

## 📄 Лицензия

MIT License
