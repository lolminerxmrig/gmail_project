import multiprocessing
from register import main

if __name__ == '__main__':
    lock = multiprocessing.Lock()
    current_processes = 0
    for _ in range(1):  # Сколько раз выполнить?
        m = multiprocessing.Process(target=main, args=(lock,))
        m.start()
        current_processes += 1
        if current_processes >= 1:  # Сколько потоков запустить?
            m.join()
            current_processes = 0
            m.terminate()
