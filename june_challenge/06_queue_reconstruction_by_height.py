class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        queue = []
        people.sort(key=lambda x: (-x[0], x[1]))

        for height, position in people:
            queue.insert(position, [height, position])

        return queue
