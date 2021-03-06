from ring import Ring
from pin import Pin


class Tower(Ring, Pin):
    def __init__(self, number_of_rings):
        self._registrator = number_of_rings
        self._number_of_moviments = 0
        self.set_pins()
        self.set_rings(number_of_rings)
        self.run_tower(self._registrator, 1, 3, 2)
        self.result(number_of_rings)

    def set_pins(self):
        pinOne = Pin()
        pinTwo = Pin()
        pinThree = Pin()
        self.pins = [pinOne, pinTwo, pinThree]

    def set_rings(self, number_of_rings):
        RING_RANGE = range(number_of_rings + 1, 1, -1)
        pinOne = self.pins[0]
        for ring_size in RING_RANGE:
            ring = Ring(ring_size)
            pinOne.insert_ring(ring)

    def move_ring(self, remove, insert):
        initial_ring_position = self.pins[remove - 1]
        final_pin_position = self.pins[insert - 1]

        moving_ring = initial_ring_position.remove_ring()
        final_pin_position.insert_ring(moving_ring)

    def run_tower(self, number_of_ring, origin, destination, auxiliary):

        if(number_of_ring > 0):
            self.run_tower(number_of_ring - 1 , origin, auxiliary, destination)
            self.move_ring(origin, destination)
            self._number_of_moviments += 1
        #    print("DISCO {} MOVED FROM PIN {} TO PIN {}".format(number_of_ring, auxiliary, destination))
            self.run_tower(number_of_ring -1, auxiliary, destination, origin)

    def result(self, number_of_rings):
        main_text = "The minimum number of moviments for {} rings is  ".format(number_of_rings)
        print(main_text + str(self._number_of_moviments))
