import random
def get_random_dish():
    dishes = ["Борщ", "Солянка", "Рассольник", "Куриный суп", "Щи", "Окрошка", "Жаркое", "Гуляш", "Плов с барбарисками"]
    return random.choice(dishes)
while True:
    user_input = input("Вы: ")
    if "приготовить" in user_input:
        bot_response = get_random_dish()
    else:
        bot_response = "Задайте вопрос правильно"
    print("Бот:", bot_response)