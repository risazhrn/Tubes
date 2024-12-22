import copy
import random
import time

class StationeryItem:
    def __init__(self, name, brand, year, sku, price, category):
        self.name = name
        self.brand = brand
        self.year = year
        self.sku = sku
        self.price = price
        self.category = category

    def __repr__(self):
        return f"{self.name} ({self.price}) - {self.category}"

def iterative_merge_sort(stationery):
    """Sorts a list of StationeryItems by price using iterative merge sort."""
    stationery_copy = copy.deepcopy(stationery)
    n = len(stationery_copy)
    width = 1
    while width < n:
        l = 0
        while l < n:
            r = min(l + 2 * width - 1, n - 1)
            m = min(l + width - 1, n - 1)
            merged = []
            i = l
            j = m + 1
            while i <= m and j <= r:
                if stationery_copy[i].price <= stationery_copy[j].price:
                    merged.append(stationery_copy[i])
                    i += 1
                else:
                    merged.append(stationery_copy[j])
                    j += 1
            while i <= m:
                merged.append(stationery_copy[i])
                i += 1
            while j <= r:
                merged.append(stationery_copy[j])
                j += 1
            stationery_copy[l:r + 1] = merged
            l += 2 * width
        width *= 2
    return stationery_copy

def recursive_merge_sort(stationery):
    """Sorts a list of StationeryItems by price using recursive merge sort."""
    stationery_copy = copy.deepcopy(stationery)
    if len(stationery_copy) <= 1:
        return stationery_copy

    mid = len(stationery_copy) // 2
    left_half = recursive_merge_sort(stationery_copy[:mid])
    right_half = recursive_merge_sort(stationery_copy[mid:])

    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i].price < right_half[j].price:
            stationery_copy[k] = left_half[i]
            i += 1
        else:
            stationery_copy[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        stationery_copy[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        stationery_copy[k] = right_half[j]
        j += 1
        k += 1
    return stationery_copy

if __name__ == "__main__":
    # Generate 300 random data
    categories = ["Alat Tulis", "Produk Kertas", "Aksesoris & Perlengkapan"]
    stationery = []
    for i in range(20):
        stationery.append(StationeryItem(
            name=f"Item {i+1}",
            brand=f"Brand {random.choice(['A', 'B', 'C', 'D', 'E'])}",
            year=random.randint(2020, 2024),
            sku=f"SKU{i+1}",
            price=random.randint(1000, 20000),
            category=random.choice(categories)
        ))

    # Sorting and displaying all data
    start_time = time.time()
    sorted_stationery_loop = iterative_merge_sort(stationery)  # Default is iterative sort
    print(f"Elapsed time for iterative merge sort: {(time.time() - start_time) * 1000} ms")

    start_time = time.time()
    sorted_stationery_recursive = recursive_merge_sort(stationery)  # Default is iterative sort
    print(f"Elapsed time for recursive merge sort: {(time.time() - start_time) * 1000} ms")

    # print("\nDaftar produk diurutkan berdasarkan harga (termurah dulu):")
    # for item in sorted_stationery_loop:
    #     print(item)
    #
    # for item in sorted_stationery_recursive:
    #     print(item)


