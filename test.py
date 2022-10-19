#%%
def f(n):
    res = 1
    for i in range(n):
        res = res * (i+1)
    return res
n = 2
print(f'f({n}) = {f(n)}')
print(f'f({n**2}) = {f(n**2)}')
#%%
data = [['sensor 1',[0.1, 0.2, 0.3]],['sensor 2',[-0.1, -0.2, -0.3, 1.4]]]
print(data[0][0])
print(data[0][0][-1])
print(data[1][1][::2])
#%%
counter = 0
value = counter + 1
while True:
    if value >= 5:
        break
    value = counter + 1
    counter += 1
print(f'Value is {value}')
print(f'Counter is {counter}')
#%%
camera0 = {}
camera0['width'] = 1920
camera0['height'] = 1080
camera0['image'] = [[1, 0, 1],[0, 1, 0]]
for item in camera0:
    print(item)
#%%

#%%
def quadratic_function(a,b,c,x):
    return a*x**2+b*x+c
y = quadratic_function(1,2,0,0.5)
#%%
b,a = ((1,2),(3,4))
d,c = 1,2
#%%
a = 4
b = 6
def divide(a,b):
    if b == 0:
        raise ZeroDivisionError('b not allowed to be zero.')
    return a / b
c = divide(2.0, 1.0)

#%%
message = ['Client 11', 1.0, 'Client 23', 0.5, 'Client 55', -2.0]

def split_data(message):
    client = message[0::2]
    values = message[1::2]
    return client,values

#%%
class ChatServer:
    """Partly implemented chat server class."""
    def __init__(self,max_connections):
        self.max_connections = max_connections
        self.connections = []
        self.nr_connections = len(self.connections)
        self.messages = {}
    def connect(self):
        if len(self.connections) >= self.max_connections:
            raise RuntimeError('Cannot connect, maximum achieved.')
        self.connections.append(self.nr_connections)
        self.nr_connections += 1
        return self.connections[-1]
    def send_message(self,to_connection,message):
        if not (to_connection in self.connections):
            raise RuntimeError('to_connection not in connections')
        self.messages[to_connection] = message
    def get_message(self,connection):
        return str(connection) + '> ' + self.message[connection]
cs_a = ChatServer(20)
cs_b = ChatServer(1)
client_1 = cs_a.connect()
client_2 = cs_a.connect()
cs_a.send_message(client_1,'Message 1')
cs_a.send_message(client_1,'Message 2')
print(cs_a.get_message(client_1))
print(cs_a.get_message(client_1))
print(cs_a.get_message(client_2))
client_3 = cs_b.connect()
cs_b.send_message(client_1,'Message 4')
print(cs_b.get_message(client_3))
# %%
