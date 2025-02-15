import time
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w',encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            word = f"Какое-то слово № {i}"
            file.write(word + '\n')
            time.sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")

# Синхронная запись
start_time = time.time()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
end_time = time.time()
print(f"Время выполнения синхронных операций: {end_time - start_time} секунд")

# Многопоточная запись
start_time = time.time()
threads = []
for word_count, file_name in [(10, "example5.txt"), (30, "example6.txt"),
                              (200, "example7.txt"), (100, "example8.txt")]:
    thread = threading.Thread(target=write_words, args=(word_count, file_name))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
print(f"Время выполнения многопоточных операций: {end_time - start_time} секунд")