# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        vals = self.preOrder(root)

        return ' '.join(vals)

    def preOrder(self, root) -> List[str]:
        if root is None:
            return ['.']

        else:
            lst = [str(root.val)]
            lst.extend(self.preOrder(root.left))
            lst.extend(self.preOrder(root.right))

            return lst

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.i = 0

        return self.build(data.split(' '))

    def build(self, data: List[str]) -> TreeNode:
        if self.i >= len(data):
            return None

        if data[self.i] == '.':
            self.i += 1
            return None
        else:
            tree = TreeNode(int(data[self.i]))
            self.i += 1
            tree.left = self.build(data)
            tree.right = self.build(data)

            return tree

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
