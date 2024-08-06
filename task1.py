import sys

def generate_circular_array(n):
    return list(range(1, n + 1))

def find_path(n, m):
    circular_array = generate_circular_array(n)
    path = []
    current_index = 0

    while True:
        path.append(circular_array[current_index])
        current_index = (current_index + m - 1) % n
        if current_index == 0:
            break

    return path

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python task1.py <n> <m>")
        sys.exit(1)
    
    n = int(sys.argv[1])
    m = int(sys.argv[2])

    path = find_path(n, m)
    print("".join(map(str, path)))
