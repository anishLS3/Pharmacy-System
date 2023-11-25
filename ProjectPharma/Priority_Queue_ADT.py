import heapq


class PriorityQueue:
    """
    Priority queue implementation using heapq module.
    """

    def __init__(self):
        """
        Initialize the priority queue.
        """
        self._queue = []
        self._index = 0

    def is_empty(self):
        """
        Check if the priority queue is empty.

        Returns:
            bool: True if the priority queue is empty, False otherwise.
        """
        return len(self._queue) == 0

    def insert(self, item, priority):
        """
        Insert an item with a priority into the priority queue.

        Args:
            item: The item to insert.
            priority: The priority of the item.
        """
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def remove(self):
        """
        Remove and return the item with the highest priority from the priority queue.

        Returns:
            The item with the highest priority.

        Raises:
            IndexError: If the priority queue is empty.
        """
        if not self.is_empty():
            return heapq.heappop(self._queue)[-1]
        raise IndexError("Priority queue is empty")
