import threading
# def do_this(what):
#     whoami(what)
# def whoami(what):
#     print("Thread %s says: %s" % (threading.current_thread(), what))
# if __name__ == '__main__':
#     whoami("I'm the main program")
#     for n in range(4):
#         p = threading.Thread(target=do_this, args=("I'm function %s" % n,))
#         p.start()

class Worker(threading.Thread):

    def run(self):
        for _ in range(1000):
            print('hello from', threading.current_thread().name)

# создаем 10 потоков
for _ in range(10):
    thread = Worker()
    # запускаем созданный поток
    thread.start()
