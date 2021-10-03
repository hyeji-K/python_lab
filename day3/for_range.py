elements = []

for i in range(0, 6):
    print(f"리스트에 {i}값을 추가합니다.")
    # append는 리스트의 함수 
    elements.append(i)

for i in elements:
    print(f"원소 {i}번쨰 값: {i}")

for i in range(10, 20, 3):
    print(i)

range(10, 20, 2)
list(range(10, 20, 2))
tuple(range(10, 20, 2))