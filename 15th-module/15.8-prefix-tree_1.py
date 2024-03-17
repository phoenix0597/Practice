# Дерево префиксов, также известное как Trie, представляет собой структуру данных, которая используется
# для эффективного поиска и хранения строк. Оно широко применяется в задачах автодополнения, поиска слов в словаре
# и многих других.
#
# Вот простая реализация дерева префиксов на Python:
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_word
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Объяснение кода:
#
# Класс TrieNode представляет узел в дереве префиксов. Каждый узел имеет словарь children,
# который содержит ссылки на дочерние узлы, и флаг is_end_word, который указывает, является ли этот узел
# концом какого-либо слова.
#
# Класс Trie представляет само дерево префиксов. Он имеет корневой узел root, который инициализируется
# при создании объекта.
#
# Метод insert(word) добавляет новое слово word в дерево префиксов. Он проходит по символам слова,
# создавая новые узлы по мере необходимости. После добавления последнего символа слова,
# флаг is_end_word устанавливается в True.
#
# Метод search(word) проверяет, содержится ли слово word в дереве префиксов. Он проходит по символам слова,
# переходя от узла к узлу. Если на каком-то шаге символ не найден в дочерних узлах,
# значит слово отсутствует в дереве. Если все символы слова были успешно пройдены,
# метод возвращает значение флага is_end_word последнего узла.
#
# Метод starts_with(prefix) проверяет, есть ли в дереве префиксов слова, начинающиеся с данного префикса prefix.
# Он работает аналогично методу search, но не проверяет флаг is_end_word в конце.
#
# Пример использования:

trie = Trie()
trie.insert("apple")
trie.insert("banana")
trie.insert("orange")

print(trie.search("apple"))  # True
print(trie.search("banana"))  # True
print(trie.search("orange"))  # True
print(trie.search("pear"))  # False

print(trie.starts_with("app"))  # True
print(trie.starts_with("ban"))  # True
print(trie.starts_with("per"))  # False

# В этом примере мы создаем объект Trie, добавляем в него три слова, затем проверяем наличие этих слов
# и префиксов с помощью методов search и starts_with.
#
# Дерево префиксов обеспечивает эффективный поиск и вставку строк, так как время выполнения операций зависит
# от длины строки, а не от количества строк в структуре данных. Это делает его подходящим для задач,
# связанных с обработкой большого количества строк.
