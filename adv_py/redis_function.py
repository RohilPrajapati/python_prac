import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

if __name__ == "__main__":
    # string operation
    print("-"*64)
    print("String Operations")
    r.set('name','Rohil Prajpati')
    name = r.get('name')
    print(f"Name: {name}")

    r.set("counter","1")
    r.incr('counter')
    r.incr('counter')
    r.decr('counter')
    counter = r.get('counter')
    print(counter)

    r.append('name',' Prajapati')
    name = r.get('name')
    print(name)

    # hash operations (like a python dict)
    print("-"*64)
    print("Hash Operations")
    r.hset('user:1','name','Ram')
    hash_user = r.hget('user:1','name')
    print(f"hash_user: {hash_user}")

    hash_obj = r.hgetall('user:1')
    print(f"hash_obj: {hash_obj}")

    # hmset is depreciated
    r.hset("user:2",mapping={'age':20,'country':"Nepal"})

    hash_obj_2 = r.hgetall("user:2")
    print(hash_obj_2)

    h_keys = r.hkeys("user:2")
    print(f"h_keys : {h_keys}")

    h_vals = r.hvals("user:2")
    print(f"h_vals : {h_vals}")

    # list operation
    print("-"*64)
    print("List Operations")
    # push to the left
    r.lpush('tasks','task1')
    # push to the right
    r.rpush('tasks','task2')

    # get all the elements
    tasks = r.lrange('tasks',0, -1)
    print(f"task: {tasks}")

    # pop from the left
    r.lpop('tasks')
    # pop from the right
    r.rpop('tasks')

    # get all the elements
    tasks = r.lrange('tasks',0, -1)
    print(f"task: {tasks}")

    # set operation (unordered, unique)
    print("-"*64)
    print("Set Operations")
    # add set value
    r.sadd('tags','python','redis')

    set_members = r.smembers('tags')
    print(f"set_members: {set_members}")

    # remove a member
    r.srem('tags','python')

    is_member = r.sismember('tags','redis')
    print(f"is_member: {is_member}")

    is_member = r.sismember('tags','python')
    print(f"is_member: {is_member}")

    # sorted set operation (ordered by  score)
    print("-"*64)
    print("Sorted Set Operations")

    r.zadd('scores', {'Ramu': 50, 'Sita': 80})
    sorted_set = r.zrange('scores',0,-1)
    print(f"sorted_set : {sorted_set}")

    rev_sorted_set = r.zrevrange('scores',0,-1)
    print(f"sorted_set : {sorted_set}")

    scores_member = r.zscore('scores','Sita')
    print(f"scores_member: {scores_member}")

    # key Management Command
    print("-"*64)
    print("Key Management commands")
    # check if key exists
    is_name_exists =  r.exists('name')
    print(f"is_name_exists: {is_name_exists}")

    # delete key
    r.delete('name')

    # make counter in 60 second
    r.expire('counter',60)

    # set time to live 
    ttl = r.ttl('counter')
    print(f"ttl: {ttl}")

    # show all the keys
    all_keys = r.keys('*')
    print(f"all_keys: {all_keys}")












    
    
