#Восстановление пароля
recover_password_button = "//a[text()='Восстановить пароль']"  # кнопка Восстановить пароль на главной странице
password_recovery_input_field = "//input[@type = 'text']" #поле ввода восстановления пароля, когда пароль видно
password_recovery_input_field_hidden = "//input[@type = 'password']" #поле ввода восстановления пароля, когда пароль скрыт
active_password_entry_field_window_in_the_password_recovery_form = "//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']" #активное окно поля ввода пароля в форме восстановления пароля
reset_password_button_on_the_recovery_page = "//button[text()='Восстановить']" #кнопка Восстановить пароль на страницу восстановления
entering_password_in_the_password_recovery_form = "//input[@name = 'Введите новый пароль']" #поле ввода пароля в форме восстановления пароля
eye_button = "//div[@class = 'input__icon input__icon-action']" #кнопка показать скрыть пароль

#Авторизация
registration_email_entry_field = './/label[text()="Email"]/following-sibling::input' #поле ввода почты
registration_name_entry_field = './/label[text()="Имя"]/following-sibling::input' #поле ввода имени
registration_password_entry_field = "//input[@class='text input__textfield text_type_main-default' and @type = 'password']" #поле ввода пароля
register_button = "//button[text()='Зарегистрироваться']"
login_button = "//button[text()='Войти']" #кнопка войти

#главная страница
personal_account_button = "//p[text()='Личный Кабинет']"  #кнопка личный кабинет
button_constructor = "//a[@class = 'AppHeader_header__link__3D_hX']" #кнопка конструктор
feed_orders = "//p[@class='AppHeader_header__linkText__3q_va ml-2'  and text() = 'Лента Заказов' ]" #Лента заказов
pink_bun = "//p[@class='BurgerIngredient_ingredient__text__yp3dH'  and text() = 'Флюоресцентная булка R2-D3' ]" # розовая булочка
window_with_details = "//h2[@class='Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10'  and text() = 'Детали ингредиента' ]" #окно с деталями булочки
cross = "(//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK' and @type='button'])[1]" #кнопка крестик на модальном окне булочки
place_to_move_the_bun = "//ul[@class = 'BurgerConstructor_basket__list__l9dp_']" #место куда нужно переместить булочку
cost_of_two_buns = "//p[@class='text text_type_digits-medium mr-3'  and text() = '1976' ]" #стоимость двух булочек после их перемещения
button_place_an_order = "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg'  and text() = 'Оформить заказ' ]" # кнопка оформить заказ
text_your_order_has_begun_to_be_prepared = "//p[@class='undefined text text_type_main-small mb-2'  and text() = 'Ваш заказ начали готовить' ]" #
the_first_order_on_the_list = "(//li[@class='OrderHistory_listItem__2x95r mb-6'])[1]" #самый первый заказ в списке
order_modal_window = "//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']" #модальное окно заказа
cross_orders = "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK' and @type='button']" #крестик на модалке созданного заказа
order_number_on_the_order_modal_window = "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']" #номер заказа на модальном окне заказа
order_number_in_order_history = "//p[@class='text text_type_digits-default']" #

#Личный кабинет
history_orders_button = "//a[text() = 'История заказов']" #кнопка история заказов
exit_button = "//button[text()='Выход']"  #кнопка выход в личном кабинете

#Лента заказов
order_number_in_the_order_feed = "(//p[@class='text text_type_digits-default'])[1]" #номер заказа в ленте заказов
completed_for_all_time = "(//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[1]" #выполнено за все время
completed_today = "(//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[2]" #выполнено за сегодня
order_number_in_progress_1 = "(//li[@class='text text_type_digits-default mb-2'])[6]" #заказ в работе