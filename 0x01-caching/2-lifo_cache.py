#!/usr/bin/env python3
"""Class LIFOCache that inherits from
BaseCaching and is a caching system:

def get(self, key):
Returns the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in
self.cache_data, return None.
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """_summary_
    """

    def __init__(self):
        """_summary_
        """
        super().__init__()

    def put(self, key, item):
        """_summary_

        Args:
                        key (_type_): _description_
                        item (_type_): _description_
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                # delete the last item in the dictionary
                last_key, last_value = self.cache_data.popitem()
                print("DISCARD: {}". format(last_key))

            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key

        Args:
                        key (_type_): _description_
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)