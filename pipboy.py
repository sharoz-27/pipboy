from colorama import init, Fore
import os
import subprocess
from groq import Groq
import sys
import time

def clear_terminal():
    """Очищает терминал."""
    try:
        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
    except Exception as e:
        print(f"Ошибка при очистке терминала: {e}")

def print_flush(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)  # Задержка в секундах
    time.sleep(0.5)  # Задержка перед очисткой терминала

def print_flush2(text, delay=0.003):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)  # Задержка в секундах
    time.sleep(0.005)  # Задержка перед очисткой терминала

def print_flush3(text, delay=0.00003):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)  # Задержка в секундах
    time.sleep(0.00003)  # Задержка перед очисткой терминала


def communicate_with_model(message):
    """Взаимодействует с моделью для генерации ответа."""
    try:
        client = Groq(
            api_key="ВАШ API КЛЮЧ"
        )

        completion = client.chat.completions.create(
            model="Llama3-70b-8192",
            messages=[
                {
                    "role": "system",
                    "content": "Тебя зовут 'Pipboy 3000 LLM'. Ты говоришь на русском языке"
                },
                {
                    "role": "user",
                    "content": message
                }
            ],
            temperature=0.3,
            max_tokens=32000,
            top_p=1,
            stream=False,
            stop=None,
        )

        return completion.choices[0].message.content
    except Exception as e:
        return f"Ошибка при общении с моделью: {e}"

# Пример использования функции
first_line = "pip..."
second_line = "Вторая строка текста."

def main():
    """Основная функция программы."""
    try:
        clear_terminal()
        print_flush(first_line)
        clear_terminal()
        print_flush(first_line)
        clear_terminal()
        print_flush2(
"""
Pipboy 3000 LLM готова к общению.
Основные команды: 
- Введите 'выход', чтобы завершить.
- Введите 'очистить', чтобы удалить переписку.

""")
        while True:
            user_input = input(Fore.LIGHTGREEN_EX + "Вы: " + Fore.WHITE)
            if user_input.lower() == 'выход':
                print("До свидания!")
                break
            elif user_input.lower() == 'очистить':
                clear_terminal()
                continue
            response = communicate_with_model(user_input)
            print(Fore.YELLOW + "Pipboy 3000 LLM:" + Fore.WHITE, end=' ')
            print_flush3(response)
            print()
    except KeyboardInterrupt:
        print("\nПрограмма завершена пользователем.")

if __name__ == "__main__":
    main()