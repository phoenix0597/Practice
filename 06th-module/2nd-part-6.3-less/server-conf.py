# {
# 	"server": {
# 		"host": "127.0.0.1",
# 		"port": 8000
# 	},
# 	"config": {
# 		"ssh": {
# 			"access": True,
# 			"login": "Ivan",
# 			"password": "qwerty"
# 		}
# 	}
# }

data = dict()
# до этого что-то происходит
print(data.get('server'))
data['server'] = {
	"host": "127.0.0.1",
	"port": 8000
}
# до этого что-то происходит
if data.get('configuration', {}).get('ssh', {}).get('login', {}):
	print("В структуре уже есть логин")
print(data.get('configuration', {}).get('ssh', {}).get('login', {}))

data['configuration'] = {
	"ssh": {
		"access": True,
		"login": "Ivan",
		"password": "qwerty"
	}
}

print(data)
