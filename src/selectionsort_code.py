import time

def selectionsort(data,drawrectangle,delay):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        drawrectangle(data, ['blue' if x == i or x == min_idx else 'red' for x in range(len(data))])
        time.sleep(delay)
    drawrectangle(data, ['blue' for x in range(len(data))])
