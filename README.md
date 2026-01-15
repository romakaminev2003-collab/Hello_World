# Hello_World! Practical_task_7.5
_________________________________
  In English:
  The program takes a list of lists as input (for example, [[0, 4, 8], [‘a’, -0], [1, 5]]) and determines the first valid subarray. A valid array is an array consisting of two natural numbers, where the first number (A) must be less than the second number (B). The program then generates a random natural number N that lies within the range [A, B] and generates two staircases of the '*' character, where the number of characters in the first staircase varies from B to N, and the number of characters in the second staircase varies from A to N.

  The program consists of three functions: check_input, get_ladder, and main.

  The check_input function takes an array as input and checks its validity. If the data is correct, it returns True, otherwise it returns False.

  The get_ladder function takes a valid array as input, generates a number N, and returns a generated array of data for displaying the ladder.

  The main function takes a list of lists as input, finds the first valid subarray, passes the subarray values to the get_ladder function, and prints the result to the screen.
  
  На русском:
  Программа на вход принимает список списков (например, [[0, 4, 8], [‘a’, -0], [1, 5]]) и определяет первый валидный подмассив. Валидным считается массив, состоящий из двух натуральных чисел, при чем первое число (A) должно быть меньше второго (B). Далее программа генерирует случайное натуральное число N, которое лежит в диапазоне [А, В] и генерирует две лесенки из символа «*», где количество символов в первой лестнице варьируется от B до N, а во второй от A до N.

  Программа состоит из трех функций: check_input, get_ladder и main.

  Функция check_input принимает на вход массив, проверяет его валидность. Если данные корректны – возвращает значение True, иначе False.

  Функция get_ladder принимает на вход валидный массив, генерирует число N и возвращает сгенерированный массив данных для вывода лестницы.

  Функция main принимает на вход список списков, находит первый валидный подмассив, передает значения подмассива на функцию get_ladder и печатает на экран результат.
