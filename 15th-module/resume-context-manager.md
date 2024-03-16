## Применение контекст-менеджеров
1. Синхронизация доступа к общим ресурсам
2. Настройка среды выполнения
3. Управление подключениями к базе данных
4. Работа с временными файлами
5. Оборачивание сетевых соединений по какому-либо протоколу и т.д.

### Пример использования контекст-менеджера как обёртка по протоколу

```python
class SomeProtocol:
    def __init__(self, host, port):
        self.host, self.port = host, port
        
    def __enter__(self):
        self._client = socket()
        self._client.connect((self.host, self.port))
        return self
       
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._client.close()

    def send(self, data):
        self._client.send(data)
        return self._client.recv(1024)

    def receive(self):
        return self._client.recv(1024)


with SomeProtocol('127.0.0.1', 8080) as protocol:
    protocol.send(['get', signal])
    result = protocol.receive()