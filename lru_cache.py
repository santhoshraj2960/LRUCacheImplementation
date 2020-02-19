from collections import OrderedDict

class LRUCache(object):
    
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.lru_cache_dict = OrderedDict()

    def get_key(self, key):
        if key in self.lru_cache_dict:
            self.lru_cache_dict.move_to_end(key, last=False)
            return self.lru_cache_dict[key]
        return 'key not found'

    def set_key(self, key, value):
        if key in self.lru_cache_dict:
            self.lru_cache_dict[key] = value
            self.lru_cache_dict.move_to_end(key, last=False)
            return True
        elif len(self.lru_cache_dict.keys()) == self.max_capacity: #cache has max capacity
            least_recently_used_key = list(self.lru_cache_dict.keys())[-1]
            self.lru_cache_dict.pop(least_recently_used_key)

        self.lru_cache_dict[key] = value
        self.lru_cache_dict.move_to_end(key, last=False)
        return True

    def print_cache_keys(self):
        print ('lru_cache_keys in order of recent usage = ', list(self.lru_cache_dict.keys()))


if __name__ == '__main__':
    print ('main called')
    lruc = LRUCache(5)
    lruc.set_key('key_one', 1)
    lruc.set_key('key_two', 2)
    lruc.set_key('key_three', 3)
    lruc.set_key('key_four', 4)
    lruc.set_key('key_five', 5)
    print ('After inserting first 5 keys')
    lruc.print_cache_keys() #['key_five', 'key_four', 'key_three', 'key_two', 'key_one']
    
    lruc.set_key('key_three', 33) 
    print ('\nAfter updating key_three')
    lruc.print_cache_keys() #['key_three', 'key_five', 'key_four', 'key_two', 'key_one']
    
    print ('\nAfter inserting new key 7 when the cache is full')
    lruc.set_key('key_seven', 7)
    lruc.print_cache_keys() #['key_seven', 'key_three', 'key_five', 'key_four', 'key_two']
    
    print('\nval in key_2 = ', lruc.get_key('key_two'))
    print('After accessing key_two')
    lruc.print_cache_keys() #['key_two', 'key_seven', 'key_three', 'key_five', 'key_four']
    
    print ('\nAfter inserting new key 8 when the cache is full')
    lruc.set_key('key_eight', 8)
    lruc.print_cache_keys() #['key_eight', 'key_two', 'key_seven', 'key_three', 'key_five']
    
