from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.translate_page import TranslatePage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # створення об'єкту сторінки
    sign_in_page = SignInPage()

    # Відкриваємо сторінку https://github.com/login
    sign_in_page.go_to()

    # Виконуємо спробу увійти в систему GitHub
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # Закриваємо браузер
    sign_in_page.close()


@pytest.mark.ui
def test_check_translation():
    # створення об'єкту сторінки
    translate_page = TranslatePage()

    # Відкриваємо сторінку https://translate.google.com.ua/?hl=ua&sl=uk&tl=en
    translate_page.go_to()

    # Виконуємо спробу увійти в систему GitHub
    translate_page.try_translate("Слава Україні!")

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert translate_page.check_translated_text("Glory to Ukraine!")

    # Закриваємо браузер
    translate_page.close()


@pytest.mark.ui
def test_check_svg_button():
    # створення об'єкту сторінки
    translate_page = TranslatePage()

    # Відкриваємо сторінку https://translate.google.com.ua/?hl=ua&sl=uk&tl=en
    translate_page.go_to()

    # Виконуємо спробу увійти в систему GitHub
    translate_page.try_translate("Слава Україні!")

    # Перевіряємо, що текст кнопки "Підтверджено спільнотою" відповідає очікуванням

    assert translate_page.check_svg_button_text(
        "Користувачі Google Перекладача позначили цей переклад як правильний."
    )

    # Закриваємо браузер
    translate_page.close()
