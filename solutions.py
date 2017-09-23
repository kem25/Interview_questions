"""
Question 1
Given two strings s and t, determine whether some anagram of t is a substring
of s. For example: if s = "udacity" and t = "ad", then the function returns
True. Your function definition should look like: question1(s, t) and return a
boolean True or False.
"""

def question1(s, t):
        
  #create dict for all characters in a given string
  def create_dict(string):
    string_dict = {}
    for character in string:
      if character in string_dict:
        string_dict[character] += 1
      else:
        string_dict[character] = 1
    return string_dict
  #check if inputs exist
  if s == None or t == None:
    return False
  if type(t) != str:
    return "t is needs to be a string"
  #check if inputs are same
  if s == t:
    return True
  #check if s is longer than t
  if len(s) < len(t): 
    return False
  
  #create dicionary from the strings
  t_dict = create_dict(t)
  s_dict = create_dict(s)
  #s should have all characters in t with occurences equal to or greater than occurence in t
  for character in t_dict: 
    if character not in s_dict:
      return False
    if s_dict[character] < t_dict[character]:
      return False 
  return True
def main():
  print(question1("Udacity","ad"))
  # True
  print(question1("Udacity",2))
  # t needs to be a string
  print(question1("Udacity","au"))
  # False
  print(question1("Udacity",""))
  # True
  print(question1("Udacity","UdacityPro"))
  # False

if __name__ == '__main__':
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
def question4(T, r, n1, n2):    
    numrows = len(T)

    # to check if inputs are within bound
    if(n1>numrows):
        print("Invalid input. Make sure inputs are within bound")
    else:    
       # print(T[20][8])
        # To check if nodes belong to tree
        check = 0
        S=[n1,n2]
        s1=len(S)
        for p in range(s1) :
            for i in range(numrows):
                 if(T[S[p]][i]==1):
                    check +=1
                 if(T[i][S[p]]==1):
                     check +=1
            if(check==0):
                print(str(S[p])+' is not in tree')
                break
            else:
               # if root is greater than nodes then traverse to left(find smallest child)
                if(r>max(n1,n2)):
                    temp = 0
                    # traverse through row to find first child
                    while(temp<numrows):
                        if(T[r][temp]==1):
                            r=temp
                            # recursive call with new child as root
                            return question4(T,r,n1,n2)
                        else:
                            temp=temp+1

                # if root less than nodes then traverse right(find greatest child)           
                elif(r<min(n1,n2)):
                    #print(r)
                    temp = numrows-1
                    # iterate from reverse of row to find first  
                    while(temp>=0):
                        if(T[r][temp]==1):
                            r=temp
                            # recursive call with new child as root
                            return question4(T,r,n1,n2)
                        else:
                            temp=temp-1

                # if root lies between the two nodes then that is the LCA
                else:
                    return r

def main():
    print(question4([[0, 1, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[1, 0, 0, 0, 1],[0, 0, 0, 0, 0]],3,1,4))
    # 3

    print(question4([[0,0,0,0,0,0],[1,0,1,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,0,0,0]],3,0,2))
    # 1

    print(question4([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1], 
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],20,12,14))
    # 12

    print(question4([[0, 1, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[1, 0, 0, 0, 1],[0, 0, 0, 0, 0]],3,2,4))
    # 2 is not in Tree
 
    print(question4([[0,0,0,0,0,0],[1,0,1,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,0,0,0]],3,8,2))
    # Invalid input.Make sure inputs are within bound

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


""" Write a code and include a route that
simulates rolling two dice and returns
the result in JSON."""
from flask import Flask 
app = Flask(__name__) 
 
import json 
import random 
 
 
@app.route('/') 
def hello_world(): 
  return 'Hello World!' 
 
# Route for diceroll 
@app.route('/diceroll/JSON') 
def diceRollJSON(): 
    # random no. within limits 
    dice1 = random.randint(1, 6) 
    dice2 = random.randint(1, 6) 
    dice_total = dice1 + dice2 
    return jsonify( 
        dice1=dice1, 
        dice2=dice2, 
        diceroll=dice_total 
    ) 
 
if __name__ == '__main__': 
  app.debug = True 
  app.run()
    
