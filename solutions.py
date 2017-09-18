"""
Question 1
Given two strings s and t, determine whether some anagram of t is a substring
of s. For example: if s = "udacity" and t = "ad", then the function returns
True. Your function definition should look like: question1(s, t) and return a
boolean True or False.
"""

# definition that checks anagrams
def is_anagram(s1, s2):
    s1 = list(s1)
    s1.sort()
    return s1 == s2

# Checks if any substrings of string s
# upto certain length are anagrams with t
def question1(s, t):
    
    # check if s is string
    if type(s) != str:
        return "s is not a string"
    
    # check if t is string
    if type(t) != str:
        return "r is not a string"

    # if t is empty, always return true
    if len(t) == 0:
        return True
    # s should conatin alteast as many characters as t
    if len(s) == 0 or len(s) < len(t):
        return False
    
    # check if substrings anagram with t
    t=list(t)
    t.sort()
    for i in range(len(s)-len(t)+1):
        if is_anagram(s[i:i+len(t)],t):
            return True
    return False

def main():
    print(question1("Udacity","city"))
    # True
    print(question1("Udacity","au"))
    # False
    print(question1("Udacity",""))
    # True
    print(question1("Udacity",2))
    # r is not a string
    print(question1("Udacity","UdacityPro"))
    # False

if __name__=='__main__':
    main()

"""
Question 2
Given a string a, find the longest palindromic substring contained in a.
Your function definition should look like question2(a), and return a string.
"""
# Ckecks if palindrome
def isPalindrome(x):
    return x == x[::-1]

def question2(x):
    # check if a is string
    if type(x) != str:
        return "input is not a string"

    # check if a has alteast two characters
    if len(x) < 2:
        return "input must have more than one character"

    # check for palindrome until maximum length
    n = len(x)
    max_length = 0
    start_index = 0
    end_index = 0
    for i in range(0, n):
        for j in range(i + 1, n + 1):
            substrng = x[i:j]
            if isPalindrome(substrng):
                if len(substrng)>max_length:
                    max_length = len(substrng)
                    start_index, end_index = i, j
    # construct longest substr
    result = x[start_index:end_index]
    return result

# Main program
def main():
    print(question2("xxxyyyxxxxyyyxyyxxyyyxxtsgszx"))
    # xyyyxxxxyyyx
    print(question2(442344))
    # input is not a string
    print(question2(""))
    # input must have more than one character

if __name__ == '__main__':
    main()

"""
Question 3
Given an undirected graph G, find the minimum spanning tree within G. A minimum
spanning tree connects all vertices in a graph with the smallest possible total
weight of edges. Your function should take in and return an adjacency list
structured like this:
{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)],
 'C': [('B', 5)]}
"""

# function that uses path compression technique
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

# A function that performs union 
# (uses union by rank)
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    # Attach smaller rank tree under root of high rank tree
    # (Union by Rank)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    #If ranks are same, make one as root and increment
    # its rank by one
    else :
        parent[yroot] = xroot
        rank[xroot] += 1

# construction of MST using Kruskal's algorithm
def KruskalMST(graph, V, inv_dict):

    result =[] 

    i = 0 
    e = 0 

    # sort edges according to weights
    graph =  sorted(graph,key=lambda item: item[2])

    parent = [] ; rank = []

    # Create V subsets with single elements
    for node in range(V):
        parent.append(node)
        rank.append(0)

    # Number of edges to be taken is equal to V-1
    while e < V -1 :

        # Step 2: Pick the smallest edge and increment the index
        # for next iteration
        u,v,w =  graph[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent ,v)

        # include edge to result if no cycle is formed,
        # and increment the index for next edge
        if x != y:
            e = e + 1
            result.append([u,v,w])
            union(parent, rank, x, y)
        # Else discard the edge

    p1 = []
    final_result = {}
    for u,v,weight  in result:
        p1 = [(inv_dict[v],weight)]
        if inv_dict[u] not in final_result:
            final_result[inv_dict[u]] = p1
        else:
            final_result[inv_dict[u]] = final_result[inv_dict[u]].append(p1)

    return final_result

def question3(G):

     # To check if G is dictionary
    if type(G) != dict:
        return "G needs to be a dictionary!"

    # To check for more than one node
    if len(G) < 2:
        return "G should have more than one edge!"
    
    n = len(G)
    tmp_dict = {}
    inv_dict = {}
    count = 0
    u,v,w = None, None, None
    graph = []
    for i in G:
        tmp_dict[i] = count
        inv_dict[count] = i
        count += 1
    #print tmp_dict

    for i in G:
        for j in G[i]:
            #print tmp_dict[i], tmp_dict[j[0]], j[1]
            u,v,w = tmp_dict[i], tmp_dict[j[0]], j[1]
            graph.append([u,v,w])
    #print graph

    return KruskalMST(graph, count, inv_dict)


# Main program
def main():
    s1 = {'A': [('B', 2)],
          'B': [('A', 4), ('C', 2)],
          'C': [('A', 2), ('B', 5)]}
    print (question3(s1))
    # {'A': [('B', 2)], 'B': [('C', 2)]}
    H=123
    print(question3(H))
    # G need to be a dictinoary
    T={}
    print(question3(T))
    # G should have more than one edge

if __name__ == '__main__':
    main()

"""
Question 5
Find the least common ancestor between two nodes on a binary search tree.
The least common ancestor is the farthest node from the root that is an ancestor
of both nodes. For example, the root is a common ancestor of all nodes on the
tree, but if both nodes are descendents of the root's left child, then that left
child might be the lowest common ancestor. You can assume that both nodes are in
the tree, and the tree itself adheres to all BST properties. The function
definition should look like question4(T, r, n1, n2), where Tis the tree
represented as a matrix, where the index of the list is equal to the integer
stored in that node and a 1 represents a child node, r is a non-negative integer
representing the root, and n1 and n2 are non-negative integers representing the
two nodes in no particular order. For example, one test case might be ...
question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
"""

class Node(object):
    # Consturctor to create a new node
  def __init__(self, data):
    self.data = data
    self.right = None
    self.left = None

# Function to insert a new node at the beginning
def push_right(node, new_data):
    new_node = Node(new_data)
    node.right = new_node
    return new_node

# Function to insert a new node at the beginning
def push_left(node, new_data):
    new_node = Node(new_data)
    node.left = new_node
    return new_node

# Function to find LCA of n1 and n2. The function assumes
# that both n1 and n2 are present in BST
def lca(root, n1, n2):
    # Base Case
    if root is None:
        return None

    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if(root.data > n1 and root.data > n2):
        return lca(root.left, n1, n2)

    # If both n1 and n2 are greater than root, then LCA
    # lies in right
    if(root.data < n1 and root.data < n2):
        return lca(root.right, n1, n2)

    return root.data


def question4(mat, root, n1, n2):

    if root < 0:
        return "Error: r  cannot be the root!"
    if n1 < 0:
        return "Error: n1 needs to be an integer!"
    if n2 < 0:
        return "Error: n2 needs to be an integer!"
    # Make BST
    head = Node(root)
    head.left, head.right = None, None
    node_value = 0
    tmp_right, tmp_left = None, None
    node_list = []
    for elem in mat[root]:
        if elem:
            if(node_value>root):
                node_list.append(push_right(head, node_value))
            else:
                node_list.append(push_left(head, node_value))
        node_value += 1

    # Compares the first element in the node list for each iteration
    tmp_node = node_list.pop(0)
    while tmp_node != None:
        node_value = 0
        for elem in mat[tmp_node.data]:
            if elem:
                if(node_value>tmp_node.data):
                    node_list.append(push_right(tmp_node, node_value))
                else:
                    node_list.append(push_left(tmp_node, node_value))
            node_value += 1
        if node_list == []:
            break
        else:
            tmp_node = node_list.pop(0)

    return lca(head, n1, n2)

# Main program
def main():
    
    print(question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4))
    # 3

    print(question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          -3,
          1,
          4))
    # r cannot be the root

    print(question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          -1,
          4))
    # n1 needs to be an integer
if __name__ == '__main__':
    main()

"""
Question 5
Find the element in a singly linked list that's m elements from the end.
For example, if a linked list has 5 elements, the 3rd element from the end is
the 3rd element. The function definition should look like question5(ll, m),
where ll is the first node of a linked list and m is the "mth number from the
end". You should copy/paste the Node class below to use as a representation of
a node in the linked list. Return the value of the node at that position.
"""

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

def get_length(ll):
    # determining the length of the linkedlist and
    # checking if lined list is circular, then return -1

    # length == 1
    if ll.next == None:
        return 1
    
    length_ll = 0
    current_node = ll
    current_node2 = ll.next
    while current_node != None and current_node != current_node2:
        current_node = current_node.next
        if current_node2 != None:
            current_node2 = current_node2.next
        length_ll += 1

    if current_node == None:
        return length_ll
    else:
        return -1

def question5(ll, m):
    # check if ll is a node
    if type(ll) != Node:
        return "Error: ll not a Node!"

    # check if m is an integer
    if m < 0:
        return "m needs to be positive"
    
    # getting length og ll from def
    length_ll = get_length(ll)

    # check if ll is circular
    if length_ll == -1:
        return "Linkedlist is circular"
        
    # check if m is less than or equal to the length of ll
    if length_ll < m:
        return "m  cannot be greater than ll length"
    
    # traversing to mth last element
    current_node = ll
    for i in range(length_ll - m):
        current_node = current_node.next
        
    return current_node.data

A = Node(3)
B = Node(4)
C = Node(9)
D = Node(2)
E = Node(7)
F = Node(4)

A.next = B 
B.next = C
C.next = D 
D.next = E
E.next = F

print(question5(A, 5))
# 8
print(question5(A,-1))
#m needs to be a positive
print(question5(A,8))
# m cannot be 


    
