
# Зададим параметры книги
pages_per_book = 100
lines_per_page = 50
characters_per_line = 25
bytes_per_character = 4

# Вычислим общий объем книги в байтах
book_size_bytes = pages_per_book * lines_per_page * characters_per_line * bytes_per_character

# Объем дискеты в байтах
floppy_disk_size_mb = 1.44
floppy_disk_size_bytes = int(floppy_disk_size_mb * 1024 * 1024)

# Рассчитаем количество книг, которое помещается на дискету
number_of_books = floppy_disk_size_bytes // book_size_bytes

# Выводим результат
print(f"На дискету объемом 1,44 Мб можно поместить {number_of_books} книг(и).")