import json

class BaseError(Exception):
  pass

class LevelError(BaseError):
  def __init__(self, cur_level, req_level):
    self.message = f'Текущий уровень {cur_level}, требуется {req_level}'
    super().__init__(self.message)

class AccessError(BaseError):
  def __init__(self, user_id):
    self.message = f'Пользователь с id {user_id} не найден' 
    super().__init__(self.message)

class User:
  def __init__(self, name, user_id, access_level):
    self.name = name
    self.user_id = user_id
    self.access_level = access_level

  def __eq__(self, other):
    return self.user_id == other.user_id
    
def load_users():
  with open('users.json', 'r') as f:
    users = json.load(f)
    
    for user in users:
      user['name'] = str(user['name'])
      
    return users
    
def add_user(user):
  user_data = {
    'name': str(user.name),
    'user_id': user.user_id,
    'access_level': user.access_level
  }
  
  with open('users.json', 'r+') as f:
    users = load_users()
    users.append(user_data)
    f.seek(0)
    json.dump(users, f, ensure_ascii=False)
    
class Project:

  def __init__(self):
    self.users = load_users()
    self.cur_user = None

  def load_data(self):
    self.users = load_users()

  def login(self, name, user_id):
    for user in self.users:
      if user['user_id'] == user_id:
        self.cur_user = user
        return
    
    raise AccessError(user_id) 
    
  def add_user(self, user):
    if user.access_level >= self.cur_user['access_level']:
      raise LevelError(self.cur_user['access_level'], user.access_level)

    add_user(user)

# test     
project = Project()
project.load_data()
project.login('Иван', 1)
project.add_user(User('Анна', 4, 3))