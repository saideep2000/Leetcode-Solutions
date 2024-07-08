class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink = numBottles
        f = 0
        e = numBottles
        while e >= numExchange:
            f = e//numExchange
            e = e - (f * numExchange) + f
            drink = drink + f
        return int(drink)