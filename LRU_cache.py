
cache={}
    

def request_send(request):
    if len(cache)<4:
        cache[request]=0
    elif len(cache)==4:
        if request in cache:
            cache[request]+=1
        else:
            minimum=min(cache.values())
            keys=0
            for key,value in cache.items():
                if value==minimum:
                    keys=key
                    break
            cache.pop(keys)
            cache[request]=0
    return cache

print(request_send(1))
print(request_send(2))
print(request_send(3))
print(request_send(4))
print(request_send(5))
print(request_send(7))

