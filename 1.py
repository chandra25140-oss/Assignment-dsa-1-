"""
Problem Statement 1: Arranging Clothes in an Almirah

Algorithm:

1. Start.
2. Let the almirah have n shelves.
3. Make a list of all clothes to be stored in the almirah.
   Each cloth has a category such as formal, casual or traditional
   and a usage level such as daily, weekly or occasional.
4. Create an indirect array which stores only the index numbers
   of clothes instead of moving the actual clothes.
5. Decide a simple comparison rule:
   - Clothes used daily should be given higher priority.
   - Clothes used weekly should be placed next.
   - Clothes used occasionally should be placed at the end.
6. Sort the indirect array according to this comparison rule.
7. Arrange the clothes on shelves using the sorted indirect array:
   - Upper shelves for daily use clothes.
   - Middle shelves for weekly use clothes.
   - Lower shelves for occasionally used clothes.
8. Keep similar categories together to reduce searching time.
9. Make sure shelves are not overfilled so that space is used properly.
10. Stop.
"""

"""
1)python program:-

clothes = [("Shirt", 1), ("Jeans", 2), ("Kurta", 3)]
index = [0, 1, 2]

for i in range(len(index)):
    for j in range(i + 1, len(index)):
        if clothes[index[i]][1] > clothes[index[j]][1]:
            index[i], index[j] = index[j], index[i]

print("Almirah Arrangement:")
for i in index:
    print(clothes[i][0])

2) c program:-
#include <stdio.h>

struct Cloth {
    char name[20];
    int priority;
};

int main() {
    struct Cloth clothes[3] = {
        {"Shirt", 1},
        {"Jeans", 2},
        {"Kurta", 3}
    };

    int index[3] = {0, 1, 2}, i, j, temp;

    for (i = 0; i < 3; i++) {
        for (j = i + 1; j < 3; j++) {
            if (clothes[index[i]].priority > clothes[index[j]].priority) {
                temp = index[i];
                index[i] = index[j];
                index[j] = temp;
            }
        }
    }

    printf("Almirah Arrangement:\n");
    for (i = 0; i < 3; i++)
        printf("%s\n", clothes[index[i]].name);

    return 0;
}

3)C++ program:-
#include <iostream>
using namespace std;

struct Cloth {
    string name;
    int priority;
};

int main() {
    Cloth clothes[3] = {{"Shirt",1},{"Jeans",2},{"Kurta",3}};
    int index[3] = {0,1,2};

    for(int i=0;i<3;i++)
        for(int j=i+1;j<3;j++)
            if(clothes[index[i]].priority > clothes[index[j]].priority)
                swap(index[i], index[j]);

    cout << "Almirah Arrangement:\n";
    for(int i=0;i<3;i++)
        cout << clothes[index[i]].name << endl;

    return 0;
}

4)Java program:-
class Cloth {
    String name;
    int priority;
    Cloth(String n, int p) {
        name = n;
        priority = p;
    }
}

public class Almirah {
    public static void main(String[] args) {
        Cloth[] clothes = {
            new Cloth("Shirt",1),
            new Cloth("Jeans",2),
            new Cloth("Kurta",3)
        };

        int[] index = {0,1,2};

        for(int i=0;i<index.length;i++)
            for(int j=i+1;j<index.length;j++)
                if(clothes[index[i]].priority > clothes[index[j]].priority){
                    int t = index[i];
                    index[i] = index[j];
                    index[j] = t;
                }

        System.out.println("Almirah Arrangement:");
        for(int i : index)
            System.out.println(clothes[i].name);
    }
}
                                
                                        OR


"""

"""
Problem Statement 1: Arranging Clothes in an Almirah

Algorithm:

1. Start.
2. Store clothes with their usage priority.
   Priority:
   1 - Daily use
   2 - Weekly use
   3 - Occasional use
3. Create an indirect array that stores index values of clothes.
4. Use Quick Sort on the indirect array instead of sorting clothes directly.
5. Comparison is done using priority values.
6. After sorting, arrange clothes according to sorted indirect array.
7. Display the arranged clothes.
8. Stop.
"""

"""
1)python:-
# Clothes list (name, priority)
clothes = [
    ("Shirt", 1),
    ("Jeans", 2),
    ("Kurta", 3)
]

# Indirect array
index = [0, 1, 2]

# Quick Sort function for indirect array
def quicksort(idx, low, high):
    if low < high:
        p = partition(idx, low, high)
        quicksort(idx, low, p - 1)
        quicksort(idx, p + 1, high)

def partition(idx, low, high):
    pivot = clothes[idx[high]][1]
    i = low - 1

    for j in range(low, high):
        if clothes[idx[j]][1] <= pivot:
            i += 1
            idx[i], idx[j] = idx[j], idx[i]

    idx[i + 1], idx[high] = idx[high], idx[i + 1]
    return i + 1

# Apply quicksort
quicksort(index, 0, len(index) - 1)

# Output
print("Almirah Arrangement:")
for i in index:
    print(clothes[i][0])

2) c:-

#include <stdio.h>

struct Cloth {
    char name[20];
    int priority;
};

struct Cloth clothes[3] = {
    {"Shirt", 1},
    {"Jeans", 2},
    {"Kurta", 3}
};

int partition(int idx[], int low, int high) {
    int pivot = clothes[idx[high]].priority;
    int i = low - 1, temp;

    for (int j = low; j < high; j++) {
        if (clothes[idx[j]].priority <= pivot) {
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
    int index[3] = {0, 1, 2};

    quicksort(index, 0, 2);

    printf("Almirah Arrangement:\n");
    for (int i = 0; i < 3; i++)
        printf("%s\n", clothes[index[i]].name);

    return 0;
}


3)c++:-
#include <iostream>
using namespace std;

struct Cloth {
    string name;
    int priority;
};

Cloth clothes[3] = {
    {"Shirt",1},
    {"Jeans",2},
    {"Kurta",3}
};

int partition(int idx[], int low, int high) {
    int pivot = clothes[idx[high]].priority;
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (clothes[idx[j]].priority <= pivot) {
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

    cout << "Almirah Arrangement:\n";
    for (int i = 0; i < 3; i++)
        cout << clothes[index[i]].name << endl;

    return 0;
}


4)java:-
class Cloth {
    String name;
    int priority;

    Cloth(String n, int p) {
        name = n;
        priority = p;
    }
}

public class Almirah {
    static Cloth[] clothes = {
        new Cloth("Shirt",1),
        new Cloth("Jeans",2),
        new Cloth("Kurta",3)
    };

    static int partition(int[] idx, int low, int high) {
        int pivot = clothes[idx[high]].priority;
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (clothes[idx[j]].priority <= pivot) {
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

        System.out.println("Almirah Arrangement:");
        for (int i : index)
            System.out.println(clothes[i].name);
    }
}

"""
