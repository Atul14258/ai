import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class bfsdfs{
    static class Node{
        char data;
        Node left;
        Node right;

        Node(char data){
            this.data = data;
        }
    }

    static class BinaryTree{
        static int idx = -1;

        public static Node buildTree(char[] nodes){
            idx++;
            if(nodes[idx] == 'N'){
                return null;
            }
            Node newnode = new Node(nodes[idx]);
            newnode.left = buildTree(nodes);
            newnode.right = buildTree(nodes);

            return newnode;
        }
    }

    public static  void bfs(Node root , char goal){
        // System.out.println("The path is : ");
        Queue<Node> q = new LinkedList<>();
        q.add(root);

        while(!q.isEmpty()){
            Node currNode = q.remove();
            System.out.print(currNode.data);
            if(currNode.data == goal){
                return;
            }
            System.out.print("->");
            if(currNode.left != null){
                q.add(currNode.left);
            }
            if(currNode.right != null){
                q.add(currNode.right);
            }
        }
        System.out.println("NULL");
    }

    static boolean found = false;
    public static void dfs(Node root , char goal){
        if(root == null || root.data == 'N'){
            return;
        }
        if(root.data == goal){
            System.out.print(root.data);
            found = true;
            return;
        }
        System.out.print(root.data + "->");
        if(!found){
            dfs(root.left , goal);
        }
        if(!found){
            dfs(root.right, goal);
        } 
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        new BinaryTree();
        char[] nodes = {'a' , 'b' , 'd' , 'h' , 'N' , 'N' , 'N','e' , 'i' ,'N' , 'N',  'j' , 'N' , 'N' ,  'c', 'f', 'k', 'N', 'N', 'l','N' , 'N', 'g', 'N' , 'N'};
        Node root = BinaryTree.buildTree(nodes);
        System.out.println();
        System.out.print("This is the Tree : ");
        bfs(root, 'X');

        System.out.println("Enter the goal Node from the given tree : ");
        char goal = sc.next().charAt(0);
        System.out.println();
        System.out.print("The path in Breadth First Search from source to Goal Node is : ");
        bfs(root , goal);
        System.out.println();
        System.out.print("The path in Depth First Search from source to Goal Node is : ");
        dfs(root, goal);
    }
}

// input goal node - h