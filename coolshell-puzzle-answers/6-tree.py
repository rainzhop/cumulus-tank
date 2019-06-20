class btnode:
    def __init__(self, data = None, left = None, right = None):
        self.left = left
        self.right = right
        self.data = data 

inorder = "T, b, H, V, h, 3, o, g, P, W, F, L, u, A, f, G, r, m, 1, x, J, 7, w, e, 0, i, Q, Y, n, Z, 8, K, v, q, k, 9, y, 5, C, N, B, D, 2, 4, U, l, c, p, I, E, M, a, j, 6, S, R, O, X, s, d, z, t"
postorder = "T, V, H, o, 3, h, P, g, b, F, f, A, u, m, r, 7, J, x, e, w, 1, Y, Q, i, 0, Z, n, G, L, K, y, 9, k, q, v, N, D, B, C, 5, 4, c, l, U, 2, 8, E, I, R, S, 6, j, d, s, X, O, a, M, p, W, t, z"

inorder = inorder.split(', ')
postorder = postorder.split(', ')

def buildtree(inorder, postorder):
    root = btnode()
    if len(inorder) == 1:
        root.data = inorder[0]
        return root
    if len(inorder) == 0:
        root.data = None
        return root
    root.data = postorder[-1]
    rootindex = inorder.index(postorder[-1])
    root.left = buildtree(inorder[:rootindex], postorder[:rootindex])
    root.right = buildtree(inorder[(rootindex + 1):], postorder[rootindex:-1])
    return root

root = buildtree(inorder, postorder)


def paint(root, n):
    a = n*'-'
    if root.data == None:
        return
    print(a+str(root.data))
    if root.left:
        n = n + 1
        paint(root.left, n)
        n = n - 1
    if root.right:
        n = n + 1
        paint(root.right, n)
        n = n - 1
    return 

paint(root, 1)

def maxdep(root):
    if root.left == None and root.right == None:
        return 0
    if root.left != None and root.right == None:
        return maxdep(root.left) + 1
    if root.right != None and root.left == None:
        return maxdep(root.right) + 1
    if root.left != None and root.right != None:
        return max(maxdep(root.right), maxdep(root.left)) + 1

def maxlen(root):
    if root.left !=  None and root.right != None:
        return max(maxdep(root.left) + maxdep(root.right), maxlen(root.left), maxlen(root.right)) 
    if root.left != None and root.right == None:
        return maxdep(root.left)
    if root.right != None and root.left == None:
        return maxdep(root.right)
    if root.left == None and root.right == None:
        return 0
