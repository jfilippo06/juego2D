import random
from clases.contador import Counter
from niveles.facil.level1 import main_level1
from niveles.facil.level2 import main_level2
from niveles.facil.level3 import main_level3
from pantallas import ganaste

niveles = [(main_level1),(main_level2),(main_level3)]
random.shuffle(niveles)
niveles.append(ganaste)

COUNTER1 = Counter()
COUNTER2 = Counter()
COUNTER3 = Counter()
COUNTER4 = Counter()
COUNTER5 = Counter()
COUNTER6 = Counter()
COUNTER7 = Counter()
COUNTER8 = Counter()
COUNTER9 = Counter()
COUNTER10 = Counter()

def check_level():
    if COUNTER1.counter:
        COUNTER1.off_counter()
        return niveles[0]
    elif COUNTER2.counter:
        COUNTER2.off_counter()
        return niveles[1]
    elif COUNTER3.counter:
        COUNTER3.off_counter()
        return niveles[3]
    elif COUNTER4.counter:
        COUNTER4.off_counter()
        return niveles[4]