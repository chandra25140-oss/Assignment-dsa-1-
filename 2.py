"""
Problem Statement 2: Arranging Clothes in a Luggage Bag

Algorithm:

1. Start.
2. Prepare a list of items to be packed for the trip.
   Each item includes clothes or accessories and their purpose
   such as sightseeing, hiking or formal dinner.
3. Identify delicate clothes that need extra care.
4. Create an indirect array to store the index positions of items.
5. Define a simple comparison rule:
   - Frequently used clothes should be easily accessible.
   - Heavy clothes should be placed at the bottom.
   - Delicate clothes should be kept at the top.
6. Sort the indirect array using the above rules.
7. Pack the items in the bag according to the sorted order:
   - Bottom layer: heavy clothes
   - Middle layer: daily use clothes
   - Top layer: delicate clothes
8. Roll clothes to save space inside the bag.
9. Use separate sections or pouches for accessories.
10. Stop.


"""
"""
1) c program:-
#include <stdio.h>

struct Item {
    char name[20];
    int priority;
};

int main() {
    struct Item items[3] = {
        {"Shoes", 2},
        {"TShirt", 1},
        {"SilkDress", 3}
    };

    int index[3] = {0,1,2}, i, j, temp;

    for(i=0;i<3;i++)
        for(j=i+1;j<3;j++)
            if(items[index[i]].priority > items[index[j]].priority){
                temp = index[i];
                index[i] = index[j];
                index[j] = temp;
            }

    printf("Luggage Arrangement:\n");
    for(i=0;i<3;i++)
        printf("%s\n", items[index[i]].name);

    return 0;
}

2) python:-
items = [("Shoes",2), ("TShirt",1), ("SilkDress",3)]
index = [0,1,2]

for i in range(len(index)):
    for j in range(i+1, len(index)):
        if items[index[i]][1] > items[index[j]][1]:
            index[i], index[j] = index[j], index[i]

print("Luggage Arrangement:")
for i in index:
    print(items[i][0])


3)c++:-
#include <iostream>
using namespace std;

struct Item {
    string name;
    int priority;
};

int main() {
    Item items[3] = {{"Shoes",2},{"TShirt",1},{"SilkDress",3}};
    int index[3] = {0,1,2};

    for(int i=0;i<3;i++)
        for(int j=i+1;j<3;j++)
            if(items[index[i]].priority > items[index[j]].priority)
                swap(index[i], index[j]);

    cout << "Luggage Arrangement:\n";
    for(int i=0;i<3;i++)
        cout << items[index[i]].name << endl;

    return 0;
}


4)java:-
class Item {
    String name;
    int priority;
    Item(String n, int p) {
        name = n;
        priority = p;
    }
}

public class Luggage {
    public static void main(String[] args) {
        Item[] items = {
            new Item("Shoes",2),
            new Item("TShirt",1),
            new Item("SilkDress",3)
        };

        int[] index = {0,1,2};

        for(int i=0;i<index.length;i++)
            for(int j=i+1;j<index.length;j++)
                if(items[index[i]].priority > items[index[j]].priority){
                    int t = index[i];
                    index[i] = index[j];
                    index[j] = t;
                }

        System.out.println("Luggage Arrangement:");
        for(int i : index)
            System.out.println(items[i].name);
    }
}


                                 OR

"""
"""
Problem Statement 2: Arranging Clothes in a Luggage Bag

Algorithm:

1. Start.
2. Store items with their packing priority.
   Priority:
   1 - Daily use
   2 - Heavy items
   3 - Delicate items
3. Create an indirect array to store index positions.
4. Apply Quick Sort on the indirect array.
5. Comparison is based on priority values.
6. Pack items according to sorted order.
7. Display the packed items.
8. Stop.
"""

"""

1)python:-
# Luggage items (name, priority)
items = [
    ("Shoes", 2),
    ("TShirt", 1),
    ("SilkDress", 3)
]

# Indirect array
index = [0, 1, 2]

# Quick Sort for indirect array
def quicksort(idx, low, high):
    if low < high:
        p = partition(idx, low, high)
        quicksort(idx, low, p - 1)
        quicksort(idx, p + 1, high)

def partition(idx, low, high):
    pivot = items[idx[high]][1]
    i = low - 1

    for j in range(low, high):
        if items[idx[j]][1] <= pivot:
            i += 1
            idx[i], idx[j] = idx[j], idx[i]

    idx[i + 1], idx[high] = idx[high], idx[i + 1]
    return i + 1

# Apply quicksort
quicksort(index, 0, len(index) - 1)

# Output
print("Luggage Arrangement:")
for i in index:
    print(items[i][0])

2)c:-
#include <stdio.h>

struct Item {
    char name[20];
    int priority;
};

struct Item items[3] = {
    {"Shoes",2},
    {"TShirt",1},
    {"SilkDress",3}
};

int partition(int idx[], int low, int high) {
    int pivot = items[idx[high]].priority;
    int i = low - 1, temp;

    for (int j = low; j < high; j++) {
        if (items[idx[j]].priority <= pivot) {
            i++;
            temp = idx[i];
            idx[i] = idx[j];
            idx[j] = temp;
        }
    }
    temp = idx[i + 1];
    idx[i + 1] = idx[high];
    idx[high] = temp;

    return i + 1;
}

void quicksort(int idx[], int low, int high) {
    if (low < high) {
        int p = partition(idx, low, high);
        quicksort(idx, low, p - 1);
        quicksort(idx, p + 1, high);
    }
}

int main() {
    int index[3] = {0,1,2};

    quicksort(index, 0, 2);

    printf("Luggage Arrangement:\n");
    for (int i = 0; i < 3; i++)
        printf("%s\n", items[index[i]].name);

    return 0;
}


3)c++:-
#include <iostream>
using namespace std;

struct Item {
    string name;
    int priority;
};

Item items[3] = {
    {"Shoes",2},
    {"TShirt",1},
    {"SilkDress",3}
};

int partition(int idx[], int low, int high) {
    int pivot = items[idx[high]].priority;
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (items[idx[j]].priority <= pivot) {
            i++;
            swap(idx[i], idx[j]);
        }
    }
    swap(idx[i + 1], idx[high]);
    return i + 1;
}

void quicksort(int idx[], int low, int high) {
    if (low < high) {
        int p = partition(idx, low, high);
        quicksort(idx, low, p - 1);
        quicksort(idx, p + 1, high);
    }
}

int main() {
    int index[3] = {0,1,2};

    quicksort(index, 0, 2);

    cout << "Luggage Arrangement:\n";
    for (int i = 0; i < 3; i++)
        cout << items[index[i]].name << endl;

    return 0;
}

4)java:-
class Item {
    String name;
    int priority;

    Item(String n, int p) {
        name = n;
        priority = p;
    }
}

public class Luggage {
    static Item[] items = {
        new Item("Shoes",2),
        new Item("TShirt",1),
        new Item("SilkDress",3)
    };

    static int partition(int[] idx, int low, int high) {
        int pivot = items[idx[high]].priority;
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (items[idx[j]].priority <= pivot) {
                i++;
                int temp = idx[i];
                idx[i] = idx[j];
                idx[j] = temp;
            }
        }
        int temp = idx[i + 1];
        idx[i + 1] = idx[high];
        idx[high] = temp;

        return i + 1;
    }

    static void quicksort(int[] idx, int low, int high) {
        if (low < high) {
            int p = partition(idx, low, high);
            quicksort(idx, low, p - 1);
            quicksort(idx, p + 1, high);
        }
    }

    public static void main(String[] args) {
        int[] index = {0,1,2};

        quicksort(index, 0, 2);

        System.out.println("Luggage Arrangement:");
        for (int i : index)
            System.out.println(items[i].name);
    }
}

