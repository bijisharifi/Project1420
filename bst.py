import json
from typing import List

# DO NOT MODIFY THIS CLASS!
class Node():
    def __init__(self, key=None, keycount=None, leftchild=None, rightchild=None):
        self.key = key
        self.keycount = keycount
        self.leftchild = leftchild
        self.rightchild = rightchild

# DO NOT MODIFY THIS FUNCTION!
# For the tree rooted at root, dump the tree to a stringified JSON object and return.
# NOTE: In future projects, you'll need to write the dump code yourself,
# but here it's given to you.
def dump(root: Node) -> str:
    def _to_dict(node) -> dict:
        return {
            "key": node.key,
            "keycount": node.keycount,
            "leftchild": (_to_dict(node.leftchild) if node.leftchild is not None else None),
            "rightchild": (_to_dict(node.rightchild) if node.rightchild is not None else None)
        }
    if root is None:
        dict_repr = {}
    else:
        dict_repr = _to_dict(root)
    return json.dumps(dict_repr, indent=2)

# -----------------------------------------------------------
# For the tree rooted at root and the key given:
# If the key is not in the tree, insert it with a keycount of 1.
# If the key is in the tree, increment its keycount.
def insert(root: Node, key: int) -> Node:
    # YOUR CODE GOES HERE.
    if root is None:
        return Node(key, 1)
    elif root.key == key:
        root.keycount += 1
    elif key < root.key:
        root.leftchild = insert(root.leftchild, key)
    else: 
        root.rightchild = insert(root.rightchild, key)


    
    return root


def minNode(root: Node)-> Node:
    currNode = root
    if currNode.leftchild is None:
        return currNode
    else:
        return minNode(currNode.leftchild)
    





"""def remove(root: Node, key: int)-> Node:
    if root is None:
        return root
    elif key < root.key:
        root.leftchild = remove(root.leftchild, key)
    elif key > root.key:
        root.rightchild = remove(root.rightchild, key)
    else:
        if root.leftchild is None:
            return root.rightchild
        elif root.rightchild is None:
            return root.leftchild
        else:
            successor = minNode(root.rightchild)
            root.key = successor.key
            root.keycount = successor.keycount
            root.rightchild = remove(root.rightchild, root.key)

        return root"""

def remove(root: Node, key: int)-> Node:
    if root is None:
        return root
    elif key < root.key:
        root.leftchild = remove(root.leftchild, key)
    elif key > root.key:
        root.rightchild = remove(root.rightchild, key)
    else:
        return root.rightchild


    

    

    



    
# For the tree rooted at root and the key given:
# If the key is not in the tree, do nothing.
# If the key is in the tree, decrement its key count. If the keycount goes to 0, remove the key.
# When replacement is necessary, use the inorder successor.
"""def delete(root: Node, key: int) -> Node:
    if root is None:
        return root

    if key < root.key:
        root.leftchild = delete(root.leftchild, key)
    elif key > root.key:
        root.rightchild = delete(root.rightchild, key)
    else:
        if root.keycount > 1:
            root.keycount -= 1
        else:
            root = remove(root, key)
    return root"""

def delete(root: Node, key: int)-> Node:
    if root is None:
        return root
    elif key < root.key:
        root.leftchild = delete(root.leftchild, key)
    elif key > root.key:
        root.rightchild = delete(root.rightchild, key)
    else:
        if root.keycount > 1:
            root.keycount -= 1
        else:
            successor = minNode(root.rightchild)
            root.key = successor.key
            root.keycount = successor.keycount
            root.rightchild = remove(root.rightchild, root.key)
    return root

    

# For the tree rooted at root and the key given:
# Calculate the list of keys on the path from the root towards the search key.
# The key is not guaranteed to be in the tree.
# Return the json.dumps of the list with indent=2.
def search(root: Node, search_key: int) -> str:
    # YOUR CODE GOES HERE.
    # Then tweak the next line so it uses your list rather than None.
    
    if root is None:
        return json.dumps([], indent=2)
    
    loclist = []
    loclist.append(root.key)
    if root.key == search_key:
        return json.dumps(loclist, indent=2)
    elif root.key < search_key:
        
        res = search(root.leftchild, search_key)
    else:
        res = search(root.rightchild, search_key)

    if res:
        loclist.extend(list(res))
    
    return json.dumps(loclist, indent=2)

    

    

# For the tree rooted at root, find the preorder traversal.
# Return the json.dumps of the list with indent=2.
def preorder(root: Node) -> str:
    # YOUR CODE GOES HERE.
    # Then tweak the next line so it uses your list rather than None.
    return json.dumps(None)

# For the tree rooted at root, find the inorder traversal.
# Return the json.dumps of the list with indent=2.
def inorder(root: Node) -> str:
    # YOUR CODE GOES HERE.
    # Then tweak the next line so it uses your list rather than None.
    return json.dumps(None)

# For the tree rooted at root, find the postorder traversal.
# Return the json.dumps of the list with indent=2.
def postorder(root: Node) -> str:
    # YOUR CODE GOES HERE.
    # Then tweak the next line so it uses your list rather than None.
    return json.dumps(None)

# For the tree rooted at root, find the BFT traversal (go left-to-right).
# Return the json.dumps of the list with indent=2.
def bft(root: Node) -> str:
    # YOUR CODE GOES HERE.
    # Then tweak the next line so it uses your list rather than None.
    return json.dumps(None)

