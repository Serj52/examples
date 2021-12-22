import random
import logging


# Запись результата звонка в loq файл
def log_bot(rating):

    logging.basicConfig(level='INFO', filename='log_bot.log', format='%(asctime)s:%(message)s')
    logging.info(f'Результат: {rating}')


# Выбор типа ответов абонента по логике
def words_for_logic(logic):

    if logic is hello_logic:
        words = random.choice(words_hello_logic)
        return words
    elif logic is main_logic:
        words = random.choice(words_main_logic)
        return words

# Работа бота
def call(*args):

    logic = hello_logic  # Стартовая модель
    print('Бот: {}'.format(templates.get('hello')))  # Превый вопрос бота
    while True:
        if logic is hello_logic:  # Ветка для hello_logic
            word = words_for_logic(logic)
            print('Клиент: {}'.format(word))  # Ответ
            print('Бот: {}'.format(templates.get(hello_logic.get(word))))  # Вопрос

            if hello_logic.get(word) in main_logic_list:  # Проверка на переход в ветку main_logic
                logic = main_logic

            elif hello_logic.get(word) in hangup_logic:  # Если разговор переходит в фазу завершения по hangup_logic
                print('Звонок окончен')
                log_bot(hangup_logic.get(hello_logic.get(word)))
                break

            elif hello_logic.get(word) in forward_logic:  # Если разговор переходит в фазу завершения по forward_logic
                print('Звонок окончен')
                log_bot(forward_logic.get(hello_logic.get(word)))
                break

        elif logic is main_logic:  # Ветка для main_logic
            word = words_for_logic(logic)
            print('Клиент: {}'.format(word))
            print('Бот: {}'.format(templates.get(main_logic.get(word))))

            if main_logic.get(word) in hangup_logic:  # Если разговор переходит в фазу завершения по hangup_logic
                print('Звонок окончен')
                log_bot(hangup_logic.get(main_logic.get(word)))
                break
            elif main_logic.get(word) in forward_logic:  # Если разговор переходит в фазу завершения по forward_logic
                print('Звонок окончен')
                log_bot(forward_logic.get(main_logic.get(word)))
                break




# Описание hello_logic
hello_logic = {'NULL': 'hello_null', 'DEFAULT': 'recommend_main', 'Да': 'recommend_main',
               'Нет': 'hangup_wrong_time', 'Занят': 'hangup_wrong_time', 'Еще раз': 'hello_repeat'}

# Описание main_logic
main_logic = {'NULL': 'recommend_main', 'DEFAULT': 'recommend_repeat', '0': 'hangup_negative', '1': 'hangup_negative',
              '2': 'hangup_negative', '3': 'hangup_negative', '4': 'hangup_negative', '5': 'hangup_negative',
              '6': 'hangup_negative', '7': 'hangup_negative', '8': 'hangup_negative', '9': 'hangup_positive',
              '10': 'hangup_positive', 'Нет': 'recommend_score_negative', 'Возможно': 'recommend_score_neutral',
              'Да': 'recommend_score_positive', 'Еще раз': 'recommend_repeat', 'Не знаю': 'recommend_repeat_2',
              'Занят': 'hangup_wrong_time', 'Вопрос': 'forward'}

# Словарь для перехода с hello_logic на main_logic
main_logic_list = {'recommend_main': None, 'recommend_repeat': None, 'recommend_repeat_2': None,
                   'recommend_score_negative': None, 'recommend_score_neutral': None, 'recommend_score_positive': None,
                   'recommend_null': None, 'recommend_default': None}

# Описание hangup_logic
hangup_logic = {'hangup_positive': 'высокая оценка', 'hangup_negative': 'низкая оценка',
                'hangup_wrong_time': 'нет времени для разговора',
                'hangup_null': 'проблемы с распознаванием'}

# Описание forward_logic
forward_logic = {'forward': 'перевод на оператора'}

# Описание представлений
templates = {
    'hello': '<Name>, добрый день! Вас беспокоит компания X, мы проводим опрос удовлетворенности нашими услугами. Подскажите, вам удобно сейчас говорить?',
    'hello_null': 'Извините, вас не слышно. Вы могли бы повторить',
    'hello_repeat': 'Это компания X  Подскажите, вам удобно сейчас говорить?',
    'recommend_main': 'Скажите, а готовы ли вы рекомендовать нашу компанию своим друзьям? Оцените, пожалуйста, по шкале от «0» до «10», где «0» - не буду рекомендовать, «10» - обязательно порекомендую.',
    'recommend_repeat': 'Как бы вы оценили возможность порекомендовать нашу компанию своим знакомым по шкале от 0 до 10, где 0 - точно не порекомендую, 10 - обязательно порекомендую.',
    'recommend_repeat_2': 'Ну если бы вас попросили порекомендовать нашу компанию друзьям или знакомым, вы бы стали это делать? Если «да» - то оценка «10», если точно нет – «0».',
    'recommend_score_negative': 'Ну а от 0 до 10 как бы вы оценили бы: 0, 5 или может 7 ?',
    'recommend_score_neutral': 'Ну а от 0 до 10 как бы вы оценили ?',
    'recommend_score_positive': 'Хорошо,  а по 10-ти бальной шкале как бы вы оценили 8-9 или может 10  ?',
    'recommend_null': 'Извините вас свосем не слышно,  повторите пожалуйста ?',
    'recommend_default': 'повторите пожалуйста',
    'hangup_positive': 'Отлично!  Большое спасибо за уделенное время! Всего вам доброго!',
    'hangup_negative': 'Я вас понял. В любом случае большое спасибо за уделенное время!  Всего вам доброго.',
    'hangup_wrong_time': 'Извините пожалуйста за беспокойство. Всего вам доброго',
    'hangup_null': 'Вас все равно не слышно, будет лучше если я перезвоню. Всего вам доброго',
    'forward': 'Чтобы разобраться в вашем вопросе, я переключу звонок на моих коллег. Пожалуйста оставайтесь на линии.'}

# Варианты ответов абонента по hello_logic
words_hello_logic = ['NULL', 'DEFAULT', 'Да', 'Нет', 'Занят', 'Еще раз']

# Варианты ответов абонента по main_logic
words_main_logic = ['NULL', 'DEFAULT', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Нет', 'Возможно', 'Да',
                    'Еще раз', 'Не знаю', 'Занят', 'Вопрос']


if __name__ == '__main__':
    call(hello_logic, main_logic, hangup_logic, forward_logic, templates, words_hello_logic, words_main_logic, main_logic_list)
