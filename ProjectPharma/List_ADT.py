from array import array


class ArrayList:
    """
    ArrayList class represents a dynamic array implementation.
    """

    def __init__(self, size, value):
        """
        Initializes an ArrayList object.

        Args:
            size (int): The initial size or capacity of the ArrayList.
            value (int|list): The initial value(s) to populate the ArrayList with.

        Raises:
            ValueError: If the size argument is negative.
        """
        self._value = value
        self._capacity = size

        if type(self._value) == int:
            self._size = self._value
            self._items = array("i", [0] * self._capacity)
        else:
            self._size = len(self._value)
            self._temp = array("i", [0] * self._capacity)
            for i in range(self._size):
                self._temp[i] = self._value[i]
            self._capacity = 2 * self._size
            self._items = self._temp

    def __len__(self):
        """
        Returns the size of the ArrayList.
        """
        return self._size

    def __getitem__(self, index):
        """
        Retrieves the element at the specified index.

        Args:
            index (int): The index of the element to retrieve.

        Returns:
            int: The value at the specified index.

        Raises:
            IndexError: If the index is out of range.
        """
        if not 0 <= index < self._size:
            raise IndexError("Index is out of range")
        return self._items[index]

    def __setitem__(self, index, value):
        """
        Sets the element at the specified index to the given value.

        Args:
            index (int): The index of the element to set.
            value (int): The value to assign.

        Raises:
            IndexError: If the index is out of range.
        """
        if not 0 <= index < self._size:
            raise IndexError("Index is out of range")
        self._items[index] = value

    def __str__(self):
        """
        Returns a string representation of the ArrayList.
        """
        return str(self._items[: self._size])

    def _resize(self, capacity):
        """
        Resizes the internal array to the specified capacity.

        Args:
            capacity (int): The new capacity of the internal array.
        """
        temp = array("i", [0] * capacity)
        for index in range(self._size):
            temp[index] = self._items[index]
        self._items = temp
        self._capacity = capacity

    def append(self, item):
        """
        Appends an item to the end of the ArrayList.

        Args:
            item (int): The item to append.
        """
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._items[self._size] = item
        self._size += 1

    def insertion(self, index, item):
        """
        Inserts an item at the specified index in the ArrayList.

        Args:
            index (int): The index at which to insert the item.
            item (int): The item to insert.

        Raises:
            IndexError: If the index is out of range.
        """
        if not 0 <= index < self._size:
            raise IndexError("Index is out of range")
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        temp = array("i", [0] * (self._size + 1))
        for i in range(len(temp)):
            if i < index:
                temp[i] = self._items[i]
            elif i == index:
                temp[i] = item
            else:
                temp[i] = self._items[i - 1]
        self._items = temp
        self._size += 1

    def deletion(self, index):
        """
        Deletes the item at the specified index from the ArrayList.

        Args:
            index (int): The index of the item to delete.

        Raises:
            IndexError: If the index is out of range.
        """
        if not 0 <= index < self._size:
            raise IndexError("Index is out of range")
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        temp = array("i", [0] * (self._size - 1))
        for i in range(len(temp)):
            if i < index:
                temp[i] = self._items[i]
            elif i >= index:
                temp[i] = self._items[i + 1]
        self._items = temp
        self._size -= 1
        if self._size <= (0.25 * self._capacity):
            self._resize(int(0.5 * self._capacity))
