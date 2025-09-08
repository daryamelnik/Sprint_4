from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    # def test_add_new_book_add_two_books(self):
    #     # создаем экземпляр (объект) класса BooksCollector
    #     collector = BooksCollector()

    #     # добавляем две книги
    #     collector.add_new_book('Гордость и предубеждение и зомби')
    #     collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # # проверяем, что добавилось именно две
        # # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        # assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    def test_get_book_genre_returns_genre(self):
        collector = BooksCollector()
        book_name = 'Гордость и предубеждение и зомби'
        book_genre_mock = 'Ужасы'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre_mock)
        book_genre = collector.get_book_genre(book_name)
        assert book_genre == book_genre_mock


    def test_get_books_genre_returns_empty_dict(self):
        collector = BooksCollector()
        books_genre = collector.get_books_genre()
        assert books_genre == {}


    def test_get_books_genre_returns_dict_with_genre(self):
        collector = BooksCollector()
        book_name = 'Гордость и предубеждение и зомби'
        book_genre_mock = 'Ужасы'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre_mock)
        books_genre = collector.get_books_genre()
        assert books_genre == {book_name: book_genre_mock}


    def test_get_list_of_favorites_books_returns_book(self):
        collector = BooksCollector() 
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        list_of_favorites_books = collector.get_list_of_favorites_books()
        assert 'Гордость и предубеждение и зомби' in list_of_favorites_books


    def test_get_list_of_favorites_books_returns_empty(self):
        collector = BooksCollector()
        list_of_favorites_books = collector.get_list_of_favorites_books()
        assert len(list_of_favorites_books) == 0


    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector() 
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        book_from_favorites = collector.get_list_of_favorites_books()
        assert 'Гордость и предубеждение и зомби' not in book_from_favorites


    def test_delete_book_from_favorites_no_effect_if_not_exists(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        book_from_favorites = collector.get_list_of_favorites_books()
        assert len(book_from_favorites) == 1
        assert 'Гордость и предубеждение и зомби' in book_from_favorites


    def test_set_book_genre_none_does_nothing(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Смешнявки')
        book_genre = collector.get_book_genre('Гордость и предубеждение и зомби')
        assert '' == book_genre


    def test_get_books_with_specific_genre_returns_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')
        books_with_specific_genre = collector.get_books_with_specific_genre('Детективы')
        assert 'Что делать, если ваш кот хочет вас убить' in books_with_specific_genre

    def test_get_books_for_children_returns_child_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')
        collector.add_new_book('Три кота')
        collector.set_book_genre('Три кота', 'Мультфильмы')
        books_for_children = collector.get_books_for_children()
        assert len(books_for_children) == 1
        assert 'Три кота' in books_for_children