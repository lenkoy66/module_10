# Потоковая запись в файлы
import time
from datetime import timedelta
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for x in range(1, word_count + 1):
            file.write(f'Какое-то слово № {x}' + '\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

# 1
list_ = [(10, 'example1.txt'), (30, 'example2.txt'), (200, 'example3.txt'), (100, 'example4.txt')]
start_time = time.time()
for count, file_ in list_:
    write_words(count, file_)
end_time = time.time()
elapsed_time = timedelta(seconds=end_time - start_time)
print(elapsed_time)

# 2
list_2 = [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]

threads = []
start_time2 = time.time()

for i in list_2:
    thread = threading.Thread(target=write_words, args=i)
    threads.append(thread)

for t in threads:
    t.start()

for t in threads:
    t.join()

end_time2 = time.time()
elapsed_time2 = timedelta(seconds=end_time2 - start_time2)

print(elapsed_time2)



