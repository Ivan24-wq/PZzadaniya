import threading
import time
import random
class Phylofod(threading.Thread):
    def __init__(sef, name, right_fork, left_fork):
        dinner().__init__()
        self.name = name
        right.fork = right_fork
        left.fort = left_fork

    def run(self):
        while True:
            print(f"{self.name} Философ размышляет!")  # Философ "размышляет"
            time.sleep(random.uniform(1.3))

            #Философ пытается взять вилку
            print(f"{self.name} Попытка взять вилку")
            self.dine()

     #ИСпользуем порядок блокировки, чтобы избежать зависания
    def dine(self):
        first_fork, second_fork = ((self.left_fork, self.right_fork) if id(self.left_fork) < id(self.right_fork) else (self.right_fork, self.left_fork))
        with first_fork:
            print(f"{self.name} Философ взял первуб вилку")
            with second_fork:
                print(f"{self.name} Философ взфл вторую вилку")
                time.sleep(random.uniform(1.3))
                print(f"{salf.name} Философ закончил есть и положит вилки на стол")
#Условие задачи
                