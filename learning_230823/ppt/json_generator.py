"""
mouckup JSON generator
파일 하나 만들어서 자유롭게 접근해보자
"""

import random
import json

# 명사 목록
nouns = ["apple", "banana", "cat", "dog", "elephant", "fish", "grape", "hat", "ice", "juice"]


def generate_random_key():
    return random.choice(nouns)


def generate_random_value(depth):
    if depth == 0:
        choices = [random.randint(1, 100), random.choice(nouns),
                   [random.choice(nouns) for _ in range(random.randint(1, 3))]]
        return random.choice(choices)
    else:
        return {generate_random_key(): generate_random_value(depth - 1) for _ in range(random.randint(1, 3))}


def generate_random_json(keys, depth):
    return {generate_random_key(): generate_random_value(depth) for _ in range(keys)}


# 예제 사용
random_json = generate_random_json(2, 5)

# JSON 파일로 저장
with open('random_nouns_with_list.json', 'w') as file:
    json.dump(random_json, file, indent=4)

# 생성된 JSON 출력
print(json.dumps(random_json, indent=4))
