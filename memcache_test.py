import memcache

db = memcache.Client(['127.0.0.1:11211'])
print(db.set('marco', 'polo'))
