import java.util.Scanner;

class Tree {
    String data;
    Tree leftNode;
    Tree rightNode;

    public Tree(String data, Tree left, Tree right) {
        this.data = data;
        this.leftNode = left;
        this.rightNode = right;
    }

    public void setLeftNode(Tree left) {
        this.leftNode = left;
    }

    public void setRightNode(Tree right) {
        this.rightNode = right;
    }

    public Tree search(String data) {
        if (this.data.equals(data)) return this;
        Tree found = null;
        if (this.leftNode != null) found = this.leftNode.search(data);
        if (this.rightNode != null && found==null) found = this.rightNode.search(data);
        return found;
    }

    public void preOrder() {
        System.out.print(data);

        if (this.leftNode != null)
            leftNode.preOrder();
        if (this.rightNode != null)
            rightNode.preOrder();

    }

    public void inOrder() {
        if (leftNode != null) leftNode.inOrder();
        if (!data.equals("."))
            System.out.print(data);
        if (rightNode != null) rightNode.inOrder();
    }

    public void postOrder() {
        if (leftNode != null) leftNode.postOrder();
        if (rightNode != null) rightNode.postOrder();
        if (!data.equals("."))
            System.out.print(data);
    }
}


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Tree sub;
        Tree tree = new Tree("A", null, null);

        for (int i = 0; i < n; i++) {
            String n1 = sc.next();
            String n2 = sc.next();
            String n3 = sc.next();

            sub = tree.search(n1);

            if(sub!=null) {
                if (!n2.equals("."))
                    sub.setLeftNode(new Tree(n2, null, null));
                if (!n3.equals("."))
                    sub.setRightNode(new Tree(n3, null, null));
            }
        }

        tree.preOrder();
        System.out.println();
        tree.inOrder();
        System.out.println();
        tree.postOrder();

    }
}
