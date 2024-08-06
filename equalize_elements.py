import sys

def read_array_from_file(file_path):
    # Чтение массива целых чисел из файла
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]

def min_moves_to_equal_elements(nums):
    # Сортировка массива для нахождения медианы
    nums.sort()
    # Вычисление медианы
    median = nums[len(nums) // 2]
    # Подсчет количества ходов для приведения всех элементов к медиане
    return sum(abs(num - median) for num in nums)

if __name__ == "__main__":
    # Проверка наличия аргумента командной строки
    if len(sys.argv) != 2:
        print("Использование: python program.py <путь_к_файлу>")
        sys.exit(1)

    file_path = sys.argv[1]
    nums = read_array_from_file(file_path)
    moves = min_moves_to_equal_elements(nums)
    print(moves)