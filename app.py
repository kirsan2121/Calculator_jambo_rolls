import streamlit as st

# Настройка страницы
st.set_page_config(page_title="Приложение для работы с печатью", layout="wide")

# Стилизация кнопок и анимации с текстом при наведении
button_style = """
    <style>
    .button {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
        height: 150px; /* Фиксированная высота кнопок */
        font-size: 16px;
        font-weight: 300 !important; /* Тонкий шрифт */
        color: #000000 !important; /* Чёрный цвет текста по умолчанию */
        text-align: center;
        text-decoration: none !important; /* Убираем подчеркивание */
        background: #F5F5F5 !important; /* Жестко установленный светло-серый фон */
        border-radius: 10px; /* Закругленные углы */
        position: relative;
        overflow: hidden;
        transition: transform 0.5s, background 1.8s ease-in-out, color 0.5s ease-in-out; /* Плавная анимация */
    }
    .button:hover {
        transform: scale(1.05); /* Увеличение при наведении */
        color: black !important; /* Чёрный текст при наведении */
    }
    .button::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 15%; /* Закрашивается только 15% кнопки */
        height: 100%;
        background: linear-gradient(135deg, rgba(28, 181, 224, 0.3), rgba(128, 0, 255, 0.3)); /* Бледное градиентное закрашивание угла */
        z-index: 1;
        opacity: 0;
        transition: opacity 0.5s ease-in-out;
    }
    .button:hover::before {
        opacity: 1; /* Показать градиент при наведении */
    }
    .button span {
        position: relative;
        z-index: 2; /* Текст всегда поверх */
    }
    </style>
"""

st.markdown(button_style, unsafe_allow_html=True)

# Главная страница с выбором блоков
def main_page():
    st.write("Выберите раздел ниже, чтобы перейти к нужному функционалу.")

    # Список секций с названием и ссылкой
    sections = [
        {"name": "Выбор печатных валов", "href": "?page=cylinders"},
        {"name": "Расчет ширины и длины печати", "href": "?page=dimensions"},
        {"name": "Калькулятор раскроя роллей", "href": "?page=rolls"},
        {"name": "Планирование тех задания", "href": "?page=planning"},
        {"name": "Загрузка входящих данных", "href": "?page=upload"},
        {"name": "Ролевая модель", "href": "?page=roles"}
    ]

    # Располагаем кнопки в 3 колонки по 2 кнопки в каждой
    cols = st.columns(3)
    for idx, section in enumerate(sections):
        with cols[idx % 3]:
            st.markdown(
                f'<a class="button" href="{section["href"]}"><span>'
                f'{section["name"]}</span></a>',
                unsafe_allow_html=True
            )

    # Форма обратной связи
    st.subheader("Обратная связь")
    with st.form("feedback_form"):
        user_email = st.text_input("Ваш email:", placeholder="example@mail.com")
        user_message = st.text_area("Ваше сообщение:", placeholder="Введите ваш отзыв или предложение...")
        submit_button = st.form_submit_button("Отправить")

        # Обработка формы
        if submit_button:
            if user_email and user_message:
                st.success("Спасибо за ваш отзыв!")
            else:
                st.error("Пожалуйста, заполните все поля.")

# Функции для разделов (placeholder)
def cylinder_selection_page():
    st.title("Выбор печатных валов")
    st.write("Настройка параметров печатных валов.")

def optimal_dimensions_page():
    st.title("Расчет ширины и длины печати")
    st.write("Расчет оптимальных размеров для печати.")

def roll_cutting_calculator_page():
    st.title("Калькулятор раскроя роллей")
    st.write("Подсчет заготовок из рулона.")

def planning_page():
    st.title("Планирование тех задания")
    st.write("Планирование технического задания.")

def upload_page():
    st.title("Загрузка входящих данных")
    st.write("Загрузка и обработка данных.")

def roles_page():
    st.title("Ролевая модель")
    st.write("Управление ролями и доступом.")

# Основное меню
page = st.query_params.get("page", ["main"])[0]

# Логика отображения страниц
if page == "main":
    main_page()
elif page == "cylinders":
    cylinder_selection_page()
elif page == "dimensions":
    optimal_dimensions_page()
elif page == "rolls":
    roll_cutting_calculator_page()
elif page == "planning":
    planning_page()
elif page == "upload":
    upload_page()
elif page == "roles":
    roles_page()
