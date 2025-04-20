class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids) == 1:
            return asteroids
        
        # making sure we have more than 2
        final = []
        final.append(asteroids[0])
        count = 1
        i = 1
        while i<len(asteroids):

            if count == 0 or asteroids[i] > 0 or final[-1] < 0:
                final.append(asteroids[i])
                count = count + 1
                i = i + 1
            else:
                if final[-1] > 0:
                    curr = final.pop()
                    count = count - 1
                    # match on the stage
                    if curr * (-1) < asteroids[i]:
                        final.append(curr)
                        count = count + 1
                        i = i + 1
                    elif curr * (-1) == asteroids[i]:
                        i = i + 1
                    # elif curr * (-1) > asteroids[i]:
                    #     final.append(asteroids[i])
                    #     count = count + 1


        return final