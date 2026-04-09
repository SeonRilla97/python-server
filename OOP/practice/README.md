# 전설의 시작

영웅이 몬스터를 물리치며 성장하는 게임

# 리스트 컴프리헨션

설명 : 리스트를 더 간결하게 표현하는 방법

```python
item_names = [item.name for item in self.inventory]
```

위 코드는 아래 코드와 동일한 기능을 한다.

```python
item_names = []
for item in self.inventory:
    item_names.append(item.name)
```
