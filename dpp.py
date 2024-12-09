import threading
import time

class Log:
    @staticmethod
    def msg(msg):
        print(msg)
    
    @staticmethod
    def delay(ms):
        time.sleep(ms / 1000.0)

class Chopstick:
    def __init__(self, name):
        self.name = name
        self.lock = threading.Lock()

    def take(self):
        self.lock.acquire()
        Log.msg(f"Used :: {self.name}")

    def release(self):
        self.lock.release()
        Log.msg(f"Released :: {self.name}")

class Philosopher(threading.Thread):
    def __init__(self, name, left_chopstick, right_chopstick):
        super().__init__()
        self.name = name
        self.left_chopstick = left_chopstick
        self.right_chopstick = right_chopstick

    def eat(self):
        with self.left_chopstick.lock:
            Log.msg(f"{self.name} picked up {self.left_chopstick.name}")
            with self.right_chopstick.lock:
                Log.msg(f"{self.name} picked up {self.right_chopstick.name}")
                Log.msg(f"{self.name} : Eat")
                Log.delay(1000)  # Simulate eating
                Log.msg(f"{self.name} : Finished eating")
        self.think()

    def think(self):
        Log.msg(f"{self.name} : Think")
        Log.delay(1000)  # Simulate thinking

    def run(self):
        for _ in range(10):  # Each philosopher eats 10 times
            self.eat()

def main():
    chopsticks = [Chopstick(f"C: {i}") for i in range(5)]
    philosophers = [
        Philosopher(f"P: {i}", chopsticks[i], chopsticks[(i + 1) % 5]) 
        for i in range(5)
    ]

    for philosopher in philosophers:
        philosopher.start()

    for philosopher in philosophers:
        philosopher.join()

if __name__ == "__main__":
    main()
