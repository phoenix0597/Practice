### Методы множеств

Метод                       Что делает метод
nums.add(elem)              добавляет элемент в множество.
nums.remove(elem)           удаляет элемент из множества. KeyError, если такого элемента не существует.
nums.discard(elem)          удаляет элемент, если он находится в множестве. Если элемента нет, то ничего не происходит
nums.pop()                  удаляет первый элемент из множества. Так как множества не упорядочены, нельзя точно сказать,
                            какой элемент будет первым.
nums.clear()                очистка множества

### Операции со множествами
A | B
A.union(B)                  Возвращает множество, являющееся объединением множеств A и B.

A |= B                  
A.update(B)                 Добавляет в множество A все элементы из множества B.

A & B
A.intersection(B)           Возвращает множество, являющееся пересечением множеств A и B.

A &= B                  
A.intersection_update(B)    Оставляет в множестве A только те элементы, которые есть в множестве B.

A - B
A.difference(B)             Возвращает разность множеств A и B (элементы, входящие в A, но не входящие в B).

A -= B
A.difference_update(B)      Удаляет из множества A все элементы, входящие в B.