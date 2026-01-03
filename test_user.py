"""
🧪 Тесты для класса User из файла polymorph.py
Для запуска: python test_user.py
"""

import unittest
from polymorph import User, UserData


class TestUserClass(unittest.TestCase):
    """Основные тесты класса User"""
    
    def test_valid_user_creation(self):
        """Тест создания валидного пользователя"""
        user = User('StalerG', 'test@example.com')
        self.assertEqual(user.username, 'StalerG')
        self.assertEqual(user.email, 'test@example.com')
        print("✅ test_valid_user_creation passed")
    
    def test_email_lowercase_conversion(self):
        """Тест авто-приведения email к нижнему регистру"""
        user = User('TestUser', 'UPPER@EXAMPLE.COM')
        self.assertEqual(user.email, 'upper@example.com')
        print("✅ test_email_lowercase_conversion passed")
    
    def test_username_too_short(self):
        """Тест: username слишком короткий (менее 3 символов)"""
        with self.assertRaises(ValueError) as context:
            User('Ab', 'test@test.com')
        self.assertIn('username', str(context.exception))
        print("✅ test_username_too_short passed")
    
    def test_username_too_long(self):
        """Тест: username слишком длинный (более 50 символов)"""
        with self.assertRaises(ValueError) as context:
            User('A' * 51, 'test@test.com')
        self.assertIn('username', str(context.exception))
        print("✅ test_username_too_long passed")
    
    def test_username_only_digits(self):
        """Тест: username только из цифр (без букв)"""
        with self.assertRaises(ValueError) as context:
            User('123456', 'test@test.com')
        self.assertIn('хотя бы одну букву', str(context.exception))
        print("✅ test_username_only_digits passed")
    
    def test_username_special_characters(self):
        """Тест: username содержит спецсимволы"""
        test_cases = ['User_Test', 'Test-User', 'User.Test', 'User@123']
        for username in test_cases:
            with self.subTest(username=username):
                with self.assertRaises(ValueError):
                    User(username, 'test@test.com')
        print("✅ test_username_special_characters passed")
    
    def test_invalid_email_format(self):
        """Тест: невалидный формат email"""
        invalid_emails = [
            'invalid-email',
            'test@',
            '@test.com',
            'test@test',
            'test@.com',
            '.test@test.com',
            'test@test..com',
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                with self.assertRaises(ValueError):
                    User('ValidUser', email)
        print("✅ test_invalid_email_format passed")
    
    def test_property_setters_valid(self):
        """Тест: валидные изменения через property-сеттеры"""
        user = User('OldUser', 'old@test.com')
        
        # Меняем username
        user.username = 'NewUser123'
        self.assertEqual(user.username, 'NewUser123')
        
        # Меняем email (авто lower())
        user.email = 'NEW@TEST.COM'
        self.assertEqual(user.email, 'new@test.com')
        
        print("✅ test_property_setters_valid passed")
    
    def test_property_setters_invalid(self):
        """Тест: невалидные изменения через property-сеттеры"""
        user = User('ValidUser', 'valid@test.com')
        
        # Пробуем невалидный username
        with self.assertRaises(ValueError):
            user.username = 'Ab'  # Слишком короткий
        
        # Пробуем невалидный email
        with self.assertRaises(ValueError):
            user.email = 'invalid'
        
        # Проверяем что оригинальные значения не изменились
        self.assertEqual(user.username, 'ValidUser')
        self.assertEqual(user.email, 'valid@test.com')
        
        print("✅ test_property_setters_invalid passed")
    
    def test_get_all_method(self):
        """Тест: метод get_all() возвращает UserData"""
        user = User('TestUser', 'test@example.com')
        user_data = user.get_all()
        
        self.assertIsInstance(user_data, UserData)
        self.assertEqual(user_data.username, 'TestUser')
        self.assertEqual(user_data.email, 'test@example.com')
        
        # Проверяем что UserData - NamedTuple (неизменяемый)
        with self.assertRaises(AttributeError):
            user_data.username = 'Hacked'
        
        print("✅ test_get_all_method passed")
    
    def test_str_method(self):
        """Тест: строковое представление пользователя"""
        user = User('StalerG', 'test@example.com')
        str_representation = str(user)
        
        self.assertIn('StalerG', str_representation)
        self.assertIn('test@example.com', str_representation)
        self.assertIn('Username:', str_representation)
        self.assertIn('Email Address:', str_representation)
        
        print("✅ test_str_method passed")
    
    def test_encapsulation_protection(self):
        """Тест: защита инкапсуляции (name mangling)"""
        user = User('Original', 'original@test.com')
        original_username = user.username
        
        # Пробуем "взломать" через name mangling
        # Это создаст новый атрибут, а не изменит существующий!
        user.__username = "HACKED"
        user._User__username = "ReallyHacked"
        
        # Проверяем что property-геттер всё ещё возвращает оригинальное значение
        self.assertEqual(user.username, original_username)
        
        print("✅ test_encapsulation_protection passed")
    
    def test_edge_cases(self):
        """Тест: граничные случаи"""
        # Минимально допустимый username (3 символа)
        user1 = User('Abc', 'test@test.com')
        self.assertEqual(user1.username, 'Abc')
        
        # Максимально допустимый username (50 символов)
        user2 = User('A' * 50, 'test@test.com')
        self.assertEqual(len(user2.username), 50)
        
        # Email с поддоменами
        user3 = User('Test', 'user.name+tag@sub.domain.co.uk')
        self.assertIn('@', user3.email)
        
        print("✅ test_edge_cases passed")


def run_all_tests():
    """Запуск всех тестов с красивым выводом"""
    print("\n" + "="*60)
    print("🧪 ЗАПУСК ТЕСТОВ ДЛЯ КЛАССА USER".center(60))
    print("="*60 + "\n")
    
    # Создаем TestSuite и запускаем
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestUserClass)
    
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite)
    
    print("\n" + "="*60)
    print("📊 РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ".center(60))
    print("="*60)
    
    if result.wasSuccessful():
        print(f"\n🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
        print(f"   Всего тестов: {result.testsRun}")
    else:
        print(f"\n❌ ЕСТЬ ПРОБЛЕМЫ:")
        print(f"   Всего тестов: {result.testsRun}")
        print(f"   Не пройдено: {len(result.failures) + len(result.errors)}")
        
        for test, traceback in result.failures + result.errors:
            print(f"\n   🔴 Провален: {test.id()}")
            print(f"      {traceback.split(chr(10))[-2]}")
    
    return result.wasSuccessful()


if __name__ == '__main__':
    # Запускаем тесты
    success = run_all_tests()
    
    # Возвращаем код выхода для CI/CD
    exit(0 if success else 1)
