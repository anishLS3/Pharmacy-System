class HashTable:
    """
    HashTable implementation using separate chaining for collision resolution.
    """

    def __init__(self, size):
        """
        Initialize the HashTable with a given size.

        Args:
            size (int): The size of the HashTable.
        """
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        """
        Hash function to calculate the index for a given key.

        Args:
            key: The key for which to calculate the index.

        Returns:
            int: The calculated index for the key.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert a key-value pair into the HashTable.

        Args:
            key: The key of the pair.
            value: The value associated with the key.
        """
        index = self._hash_function(key)
        bucket = self.table[index]
        for item in bucket:
            if item[0] == key:
                # Update value if key already exists
                item[1] = value
                return
        bucket.append([key, value])

    def search(self, key):
        """
        Search for a key in the HashTable and return its associated value.

        Args:
            key: The key to search for.

        Returns:
            The value associated with the key, or None if the key is not found.
        """
        index = self._hash_function(key)
        bucket = self.table[index]
        for item in bucket:
            if item[0] == key:
                return item[1]
        return None

    def delete(self, key):
        """
        Delete a key-value pair from the HashTable.

        Args:
            key: The key of the pair to delete.
        """
        index = self._hash_function(key)
        bucket = self.table[index]
        for i, item in enumerate(bucket):
            if item[0] == key:
                del bucket[i]
                return

    def __str__(self):
        """
        Return a string representation of the HashTable.

        Returns:
            str: The string representation of the HashTable.
        """
        output = ""
        for bucket in self.table:
            if bucket:
                output += (
                    "["
                    + ", ".join(str(item[0]) + ":" + str(item[1]) for item in bucket)
                    + "] "
                )
            else:
                output += "[ ] "
        return output
