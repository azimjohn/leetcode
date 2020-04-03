class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        if len(x) < 4:
            return False
        
        position = [0, 0]
        positions = [position[::]]
        for i, move in enumerate(x):
            self.make_move(position, move, i % 4)
            positions.append(position[::])

            if i >= 3:
                if self.crosses(positions[i], positions[i+1], positions[i-2], positions[i-3]):
                    return True
            if i >= 5:
                if self.crosses(positions[i], positions[i+1], positions[i-4], positions[i-5]):
                    return True
            if i == 4:
                if positions[i+1] == positions[i-4]:
                    return True

        return False

    def make_move(self, position, move, direction):
        if direction == 0:
            position[1] += move
        elif direction == 1:
            position[0] -= move
        elif direction == 2:
            position[1] -= move
        elif direction == 3:
            position[0] += move
 
    def crosses(self, p1, p2, p3, p4) -> bool:
        if p3[0] == p4[0] and p1[1] == p2[1]:
            p1, p2, p3, p4 = p3, p4, p1, p2

        big_x, small_x = max(p3[0], p4[0]), min(p3[0], p4[0])
        big_y, small_y = max(p1[1], p2[1]), min(p1[1], p2[1])
        return small_x <= p1[0] <= big_x and small_y <= p3[1] <= big_y
