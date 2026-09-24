import os
import sys
import platform


name_os = os.name
platform_os = sys.platform
version_os = platform.version()
release_os = platform.release()
arch_os = platform.architecture()
proc_os = platform.processor()


data_list = [name_os, platform_os, version_os, release_os, arch_os, proc_os]


titles = [
    "Название ОС (os.name)",
    "Платформа (sys.platform)",
    "Версия (platform.version)",
    "Релиз (platform.release)",
    "Архитектура (platform.architecture)",
    "Процессор (platform.processor)"
]

def print_menu():
    sys.stdout.write("\n--- Диагностика системы ---\n")
    sys.stdout.write("Выберите пункт для просмотра:\n")
    for i in range(len(titles)):
        sys.stdout.write(str(i + 1) + ". " + titles[i] + "\n")
    sys.stdout.write("0. Выход\n")
    sys.stdout.write("Введите номер: ")

def main():
    while True:
        print_menu()
        
        # Читаем ввод пользователя
        user_input = sys.stdin.readline().strip()
        
        if user_input == '0':
            sys.stdout.write("Выход из программы.\n")
            break
        
        # Проверяем, что введено число
        if user_input.isdigit():
            num = int(user_input) - 1
            if 0 <= num < len(data_list):
                sys.stdout.write("\nРезультат: " + str(data_list[num]) + "\n")
            else:
                sys.stdout.write("\nНет такого пункта.\n")
        else:
            sys.stdout.write("\nВведите число!\n")

if __name__ == "__main__":
    main()