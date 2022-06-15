from typing import (
    List
)

def bubbleSort(data: List[int]) -> List[int]:
    n: int = len(data)

    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    return data