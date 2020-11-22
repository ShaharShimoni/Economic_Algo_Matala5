# Economic_Algo_Matala5_Ques5

Given the following department: <br />
class Agent: <br />
def item_value (item_index: int) → float: ... <br />
The class represents a player participating in a fair division game. <br />
It has one function that describes the value that the player attributes to an object whose index is index_item. <br />

def envy_graph (agents: List [Agent], bundles: List [List [int]]):  <br />
function that produces the envy graph in a given division. <br />

The agents parameter is an n-size array that represents the players. <br />
The bundles parameter is an array of the same size - n - that represents the division:  <br />
bundle[i] is a collection of the objects player i receives. <br />
The function returns a graph of Python's networkx library. <br />
An examples of interesting inputs: <br />

The first example : everyone is Jealous



![דוגמא מהכיתה](https://user-images.githubusercontent.com/57682267/99914603-22650980-2d07-11eb-9e1a-2dcd7d7cefd7.png)

The Second example: no one is Jealous



![ללא קנאה](https://user-images.githubusercontent.com/57682267/99914616-3c9ee780-2d07-11eb-94ee-e935b5abe181.png)

The third example: There is a circle



![קיים מעגל](https://user-images.githubusercontent.com/57682267/99914627-56d8c580-2d07-11eb-95dc-c77601ad2f2a.png)


