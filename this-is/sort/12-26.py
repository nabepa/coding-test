# 새로 만들어진 카드에 의해 기존 순서가 바뀐다는 것에 주의
import heapq

n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

result = 0
while len(cards) >= 2:
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)
    n_card = card1 + card2
    result += n_card
    heapq.heappush(cards, n_card)

print(result)
