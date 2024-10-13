def read_data(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"A {filename} fájl nem található.")
        return None

def is_numeric_data(data):
    try:
        [float(item) for item in data]
        return True
    except ValueError:
        return False

def bubble_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if reverse:
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insert_element(arr, element, reverse=False):
    for i, item in enumerate(arr):
        if reverse:
            if element > item:
                arr.insert(i, element)
                return arr
        else:
            if element < item:
                arr.insert(i, element)
                return arr
    arr.append(element)
    return arr

def main():
    filename = "ki.txt"
    data = read_data(filename)
    
    if data is None or len(data) == 0:
        print("A fájl üres vagy nem olvasható.")
        return

    is_numeric = is_numeric_data(data)
    if is_numeric:
        data = [float(item) for item in data]
        print("A fájl számokat tartalmaz.")
    else:
        print("A fájl szövegeket tartalmaz.")

    direction = input("Válassza ki a rendezés irányát (n - növekvő, c - csökkenő): ").lower()
    reverse = direction == 'c'

    sorted_data = bubble_sort(data, reverse=reverse)
    print("Buborékrendezés eredménye:")
    print(sorted_data)

    new_element = input("Adj meg egy új elemet: ")
    if is_numeric:
        try:
            new_element = float(new_element)
        except ValueError:
            print("Érvénytelen szám.")
            return

    inserted_data = insert_element(sorted_data, new_element, reverse=reverse)
    print("Az új elem beszúrása után:")
    print(inserted_data)

if __name__ == "__main__":
    main()
