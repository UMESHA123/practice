package BinaryTree;

class Node{
    Node left = null;
    Node right = null;
    int key;

    Node(int key){
        this.key = key;
    }
}
public class BinaryTree {
    public static void main(String[] args) {
        Node root = new Node(10);
        root.left = new Node(20);
        root.right = new Node(30);
        root.left.left = new Node(40);
        root.left.right = new Node(50);
    }
}
