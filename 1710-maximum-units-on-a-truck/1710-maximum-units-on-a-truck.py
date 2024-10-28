class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        boxTypes = sorted(boxTypes, key=lambda x: x[1])
        units = 0
        while boxTypes and truckSize:
            popped = boxTypes.pop()
            if popped[0] <= truckSize:
                units += popped[0] * popped[1]
                truckSize -= popped[0]
            else:
                units += truckSize * popped[1]
                truckSize = 0
        return units
        