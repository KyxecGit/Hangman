import random
from words import words_list
from arts import logo, stages

chosen_word = random.choice(words_list) # выбор случайного слова
word_length = len(chosen_word) # длина этого слова

end_of_game = False
lives = 6

print(logo)

display = []
for _ in range(word_length): # создаем список из нижних подчеркиваний по количеству букв
    display += "_"

while not end_of_game: # игровой цикл на каждом шаге которого записываем и проверяем букву
    guess = input("Введите букву: ").lower()

    if guess in display:
        print(f"Эта буква уже была: {guess}")

    for position in range(word_length): # перебираем слово 
        letter = chosen_word[position]
        if letter == guess: # если буква есть в слове замещаем _ в списке на букву
            display[position] = letter

    if guess not in chosen_word: # отнимаем жизни если пользователь не смог угадать букву
        print(f"Ты ввел: {guess}, ее нет в этом слове. Ты потерял жизнь.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Ты проиграл. слово:",chosen_word)

    print(f"{' '.join(display)}") # превращаем наш список в строку для более красивого отображения

    if "_" not in display: # условия победы 
        end_of_game = True
        print("Ты победил.")

    print(stages[lives]) # печатаем аски рисунки в зависимости от количества жизней