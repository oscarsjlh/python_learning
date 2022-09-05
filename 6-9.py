friend = {
    'oscar': {
        'likes':'nauture',
        'first': 'Oscar'
        },
    'valentine': {
        'likes': 'sea',
        'first': 'Valentine'
        },
    'jack': {
        'likes': 'city',
        'first': 'Jack'
        },
    }

for name, friend_info in friend.items():
   name = f"{friend_info['first']}" 
   likes= f"{friend_info['likes']}"
   print(f"{name} likes {likes}")
