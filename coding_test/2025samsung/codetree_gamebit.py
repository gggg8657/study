# Input processing
H, W, N, K, A, B = map(int, input().split())

piece_names = []
piece_positions = []
for _ in range(2 * N + 2):
    name, x, y = input().split()
    piece_names.append(name)
    piece_positions.append((int(x), int(y)))

white_preferences = input().split()
black_preferences = input().split()

white_hp = list(map(int, input().split()))
black_hp = list(map(int, input().split()))

# Please write your code here.
