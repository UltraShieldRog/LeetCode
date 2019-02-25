class Solution:
    def dfs(self, root, l, f):
        if root is None:
            return
        
        self.level[root.val] = l
        self.father[root.val] = f
        self.dfs(root.left, l + 1, root.val)
        self.dfs(root.right, l + 1, root.val)
    
    def isCousins(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
        self.level = {}
        self.father = {}
        
        self.dfs(root, 0, -1)
        
        return self.level[x] == self.level[y] and self.father[x] != self.father[y]
