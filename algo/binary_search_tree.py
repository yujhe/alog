from stack_queue import ArrayQueue


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.count = 1


class RedBlackNode:
    def __init__(self, key, val, color):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.count = 1
        self.color = color.lower()  # red, black


class BST:
    def __init__(self):
        pass

    def put(self, key, val):
        pass

    def _put(self, x, key, val):
        pass

    def get(self, key):
        pass

    # return smallest key
    def min(self):
        pass

    def _min(self, x):
        pass

    # return largest key
    def max(self):
        pass

    # return largest key <= given key
    def floor(self, key):
        pass

    def _floor(self, x, key):
        pass

    # return smallest key >= given key
    def ceil(self, key):
        pass

    def _ceil(self, x, key):
        pass

    # return the count at the root
    def size(self):
        pass

    # return # of keys betweeb lo and hi
    def size_between(self, lo, hi):
        pass

    def _size(self, x):
        pass

    # return # of keys < given key
    def rank(self, key):
        pass

    def _rank(self, x, key):
        pass

    def keys(self):
        pass

    # return keys between lo and hi
    def keys_between(self, lo, hi):
        pass

    def _keys_between(self, x, lo, hi, queue):
        pass

    def _preorder(self, x, queue):
        pass

    # inorder: left -> root -> right
    def _inorder(self, x, queue):
        pass

    # postorder: left -> right -> root
    def _postorder(self, x, queue):
        pass

    def delete(self, key):
        pass

    def _delete(self, x, key):
        pass

    def delete_min(self):
        pass

    def _delete_min(self, x):
        pass


class RedBlackBST:
    def __init__(self):
        self.root = None

    def put(self, key, val):
        self.root = self._put(self.root, key, val)

    def _put(self, x, key, val):
        if x == None:
            return RedBlackNode(key, val, 'red')

        cmp = key - x.key
        if cmp < 0:
            x.left = self._put(x.left, key, val)
        elif cmp > 0:
            x.right = self._put(x.right, key, val)
        else:
            x.val = val

        # make a balanced tree
        if self._is_red(x.right) and not self._is_red(x.left):
            x = self._rotate_left(x)
        if self._is_red(x.left) and self._is_red(x.left.left):
            x = self._rotate_right(x)
        if self._is_red(x.left) and self._is_red(x.right):
            self._flip_colors(x)

        x.count = 1 + self._size(x.left) + self._size(x.right)

        return x

    def get(self, key):
        x = self.root
        while x != None:
            cmp = key - x.key
            if cmp < 0:
                x = x.left
            elif cmp > 0:
                x = x.right
            else:
                return x.val
        return None

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, x, key):
        if x == None:
            return None

        cmp = key - x.key
        if cmp < 0:
            x.left = self._delete(x.left, key)
        elif cmp > 0:
            x.right = self._delete(x.right, key)
        else:
            if x.left == None:
                return x.right
            if x.right == None:
                return x.left

            t = x
            x = self._min(t.right)
            x.right = self._delete_min(t.right)
            x.left = t.left

        x.count = 1 + self._size(x.left) + self._size(x.right)

        return x

    def _delete_min(self, x):
        if x.left == None:
            return x.right

        x.left = self._delete_min(x.left)
        x.count = 1 + self._size(x.left) + self._size(x.right)

        return x

    def _min(self, x):
        while x.left != None:
            x = x.left

        return x

    def size(self):
        return self._size(self.root)

    def _size(self, x):
        if x == None:
            return 0
        return x.count

    def _rotate_left(self, x):
        t = x.right
        x.right = t.left
        t.left = x
        t.color = x.color
        x.color = 'red'

        return t

    def _rotate_right(self, x):
        t = x.left
        x.left = t.right
        t.right = x
        t.color = x.color
        x.color = 'red'

        return t

    def _flip_colors(self, x):
        x.color = 'red'
        x.left.color = 'black'
        x.right.color = 'black'

    def _is_red(self, x):
        if x == None:
            return False
        return x.color == 'red'


if __name__ == '__main__':
    input = [
        (7, 1),
        (2, 1),
        (3, 1),
        (8, 1),
        (9, 1),
        (1, 1),
        (5, 1),
        (7, 2)]

    bst = BST()
    red_black_bst = RedBlackBST()

    for k, v in input:
        bst.put(k, v)
        red_black_bst.put(k, v)

    assert bst.get(1) == 1, f'bst.get(1)={bst.get(1)}'
    assert bst.get(2) == 1, f'bst.get(2)={bst.get(2)}'
    assert bst.get(7) == 2, f'bst.get(7)={bst.get(7)}'
    assert bst.get(8) == 1, f'bst.get(8)={bst.get(8)}'
    assert bst.get(9) == 1, f'bst.get(9)={bst.get(9)}'

    assert red_black_bst.get(1) == 1, f'red_black_bst.get(1)={red_black_bst.get(1)}'
    assert red_black_bst.get(2) == 1, f'red_black_bst.get(2)={red_black_bst.get(2)}'
    assert red_black_bst.get(7) == 2, f'red_black_bst.get(7)={red_black_bst.get(7)}'
    assert red_black_bst.get(8) == 1, f'red_black_bst.get(8)={red_black_bst.get(8)}'
    assert red_black_bst.get(9) == 1, f'red_black_bst.get(9)={red_black_bst.get(9)}'

    assert bst.min() == 1, f'bst.min()={bst.min()}'
    assert bst.max() == 9, f'bst.max()={bst.max()}'

    assert bst.floor(0) == None, f'bst.floor(0)={bst.floor(0)}'
    assert bst.floor(1) == 1, f'bst.floor(1)={bst.floor(1)}'
    assert bst.floor(2) == 2, f'bst.floor(2)={bst.floor(2)}'
    assert bst.floor(7) == 7, f'bst.floor(7)={bst.floor(7)}'
    assert bst.floor(6) == 5, f'bst.floor(6)={bst.floor(6)}'
    assert bst.floor(10) == 9, f'bst.floor(10)={bst.floor(10)}'

    assert bst.ceil(0) == 1, f'bst.ceil(0)={bst.ceil(0)}'
    assert bst.ceil(1) == 1, f'bst.ceil(1)={bst.ceil(1)}'
    assert bst.ceil(2) == 2, f'bst.ceil(2)={bst.ceil(2)}'
    assert bst.ceil(7) == 7, f'bst.ceil(7)={bst.ceil(7)}'
    assert bst.ceil(6) == 7, f'bst.ceil(6)={bst.ceil(6)}'
    assert bst.ceil(10) == None, f'bst.ceil(10)={bst.ceil(10)}'

    assert bst.size() == 7, f'bst.size()={bst.size()}'
    assert red_black_bst.size() == 7, f'red_black_bst.size()={red_black_bst.size()}'

    assert bst.rank(0) == 0, f'bst.rank(0)={bst.rank(0)}'
    assert bst.rank(1) == 0, f'bst.rank(1)={bst.rank(1)}'
    assert bst.rank(2) == 1, f'bst.rank(2)={bst.rank(2)}'
    assert bst.rank(7) == 4, f'bst.rank(7)={bst.rank(7)}'
    assert bst.rank(10) == 7, f'bst.rank(10)={bst.rank(10)}'

    keys = bst.keys()
    for idx, i in enumerate([1, 2, 3, 5, 7, 8, 9]):
        key = keys.dequeue()
        assert key == i, f'bst.keys[{idx}]={key}'

    bst.delete_min()
    assert bst.min() == 2, f'bst.min()={bst.min()}'
    assert bst.max() == 9, f'bst.max()={bst.max()}'

    bst.delete(1)
    assert bst.get(1) == None, f'bst.get(1)={bst.get(1)}'
    assert bst.min() == 2, f'bst.min()={bst.min()}'
    assert bst.max() == 9, f'bst.max()={bst.max()}'

    red_black_bst.delete(1)
    assert red_black_bst.get(1) == None, f'red_black_bst.get(1)={red_black_bst.get(1)}'

    bst.delete(5)
    assert bst.get(5) == None, f'bst.get(5)={bst.get(5)}'
    assert bst.min() == 2, f'bst.min()={bst.min()}'
    assert bst.max() == 9, f'bst.max()={bst.max()}'

    red_black_bst.delete(5)
    assert red_black_bst.get(5) == None, f'red_black_bst.get(5)={red_black_bst.get(5)}'

    bst.delete(2)
    assert bst.get(2) == None, f'bst.get(2)={bst.get(2)}'
    assert bst.min() == 3, f'bst.min()={bst.min()}'
    assert bst.max() == 9, f'bst.max()={bst.max()}'

    red_black_bst.delete(2)
    assert red_black_bst.get(2) == None, f'red_black_bst.get(2)={red_black_bst.get(2)}'

    bst.delete(9)
    assert bst.get(9) == None, f'bst.get(9)={bst.get(9)}'
    assert bst.min() == 3, f'bst.min()={bst.min()}'
    assert bst.max() == 8, f'bst.max()={bst.max()}'

    red_black_bst.delete(9)
    assert red_black_bst.get(9) == None, f'red_black_bst.get(9)={red_black_bst.get(9)}'

    keys = bst.keys()
    assert keys.q == [8, 7, 3], f'bst.keys()={keys.q}'

    assert red_black_bst.size() == 3, f'red_black_bst.size()={red_black_bst.size()}'

    assert bst.size_between(0, 1) == 0, f'bst.size(0, 1)={bst.size_between(0, 1)}'
    assert bst.size_between(1, 4) == 1, f'bst.size(1, 4)={bst.size_between(1, 4)}'
    assert bst.size_between(3, 8) == 3, f'bst.size(3, 8)={bst.size_between(3, 8)}'

    assert bst.keys_between(0, 1).q == [], f'bst.keys_between(0, 1)={bst.keys_between(0, 1)}'
    assert bst.keys_between(0, 7).q == [7, 3], f'bst.keys_between(0, 7)={bst.keys_between(0, 7)}'
    assert bst.keys_between(7, 8).q == [8, 7], f'bst.keys_between(7, 8)={bst.keys_between(7, 8)}'
    assert bst.keys_between(9, 10).q == [], f'bst.keys_between(9, 10)={bst.keys_between(9, 10)}'
