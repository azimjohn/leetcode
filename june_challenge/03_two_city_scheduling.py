class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        total_cost = 0
        costs.sort(key=lambda cost: cost[0] - cost[1])
        
        total_cost += sum([cost[0] for cost in costs[:n//2]])
        total_cost += sum([cost[1] for cost in costs[n//2:]])
        
        return total_cost
