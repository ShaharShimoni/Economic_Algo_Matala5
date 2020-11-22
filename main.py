# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import networkx as nx
from typing import List
import matplotlib.pyplot as plt

class Agent:
    stringNode="";
    wants = []    # The agent has an array of its Preferences
    def item_value(self,item_index:int)->float:
        return self.wants[item_index]

    def my_value(self,agent_index:int,bundles:List[List[int]])->float:  #value for the items the agent got
        sum=0;
        for i in bundles[agent_index]:   # items of agent "agent_index"
            sum += self.item_value(i);
        return sum;

def envy_graph(agents:List[Agent], bundles:List[List[int]]):
    G = nx.DiGraph();
    for x in agents:
        G.add_nodes_from([x.stringNode]);
    #print(G.nodes())
    #print(G.edges())
    count = 0;  #counts the num of the agent-just for me
    for x in agents:   # pass all the agents, and see if they are Jealous,if so add an edge between.
        my_sum=x.my_value(int(x.stringNode),bundles);  #value for the items the agent got
        num_of_agent = 0;
        for y in bundles:
            sum_x_eye=0;   #count how agent x see all the stuff.
            for k in y:
                sum_x_eye+=x.item_value(k);
            if sum_x_eye>my_sum: #Jealous
                 #print("Jealous");
                 G.add_edge(x.stringNode,str(num_of_agent),length = 0);
            num_of_agent=num_of_agent+1;
        count=count+1;

    #print(G.edges())
    return G;


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

#The Example from the presentation:
    yellow = Agent()
    yellow.stringNode="0";   #num of Node
    green = Agent()
    green.stringNode = "1";
    blue = Agent()
    blue.stringNode = "2";
     #Preferences:
    array1 = [1,2,3]
    array2 = [3,1,2]
    array3 = [2,3,1]
    yellow.wants = array1;
    green.wants = array2;
    blue.wants = array3;

    #What each one got:
    a=0;
    b=1;
    c=2;
    bundles=[[a],[b],[c]];

    AgentList = []
    AgentList.insert(0, yellow );
    AgentList.insert(1, green);
    AgentList.insert(2, blue);

    G=envy_graph(AgentList, bundles);
    pos = nx.spring_layout(G);
    nx.draw(G, pos, with_labels=True, connectionstyle='arc3, rad = 0.1')
    edge_labels = dict([((u, v,), d['length'])
                    for u, v, d in G.edges(data=True)]);
    plt.show();


#second example- no one is Jealous
    one = Agent()
    one.stringNode="0";   #num of Node
    two = Agent()
    two.stringNode = "1";
    three = Agent();
    three.stringNode = "2";
    arr_one = [2,2,2];
    one.wants=arr_one;
    arr_two = [2,2,2];
    two.wants=arr_two;
    arr_three = [2,2,2];
    three.wants=arr_three;

    bundles2=[[a],[b],[c]];
    AgentList2 = []
    AgentList2.insert(0, one );
    AgentList2.insert(1, two);
    AgentList2.insert(2, three);

    G2=envy_graph(AgentList2, bundles2);
    pos = nx.spring_layout(G2);
    nx.draw(G2, pos, with_labels=True, connectionstyle='arc3, rad = 0.1')
    edge_labels = dict([((u, v,), d['length'])
                   for u, v, d in G2.edges(data=True)]);
    plt.show();



#third example-There is a circle
    Ami = Agent()
    Ami.stringNode="0";   #num of Node
    Tmi = Agent()
    Tmi.stringNode = "1";
    Rmi = Agent();
    Rmi.stringNode = "2";
    Bni = Agent();
    Bni.stringNode = "3";
    arr_Ami = [5,1,3,6,1,4];
    Ami.wants=arr_Ami;
    arr_Tmi = [1,4,5,6,2,3];
    Tmi.wants=arr_Tmi;
    arr_Rmi = [3,2,6,4,5,1];
    Rmi.wants=arr_Rmi;
    arr_Bni = [2,3,5,1,6,4];
    Bni.wants=arr_Bni;

    bundles3=[[0],[1,4],[3,5],[2]];
    AgentList3 = []
    AgentList3.insert(0, Ami );
    AgentList3.insert(1, Tmi);
    AgentList3.insert(2, Rmi);
    AgentList3.insert(3, Bni);

    G3=envy_graph(AgentList3, bundles3);
    pos = nx.spring_layout(G3);
    nx.draw(G3, pos, with_labels=True, connectionstyle='arc3, rad = 0.1')
    edge_labels = dict([((u, v,), d['length'])
                   for u, v, d in G3.edges(data=True)]);
    plt.show();



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
