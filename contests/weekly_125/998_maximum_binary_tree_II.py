class Solution:
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # Recusive method
        if root is None or val > root.val:
            ret = TreeNode(val)
            ret.left = root
            return ret
        root.right = self.insertIntoMaxTree(root.right, val)
        return root
    
        ## loop method  
        # if not root or val > root.val:
        #     r = TreeNode(val)
        #     r.left = root
        #     return r
        # p, c = root, root.right
        # while c and c.val > val: 
        #     p, c = c, c.right
        # p.right = TreeNode(val)
        # p.right.left = c
        # return root
