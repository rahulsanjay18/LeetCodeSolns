class MyStack {
    public LinkedList<Integer> q1 = new LinkedList<Integer>();
    public LinkedList<Integer> q2 = new LinkedList<Integer>();
    public MyStack() {
    }
    
    public void push(int x) {
        q1.addLast(x);
        q2.addFirst(x);
    }
    
    public int pop() {
        q1.removeLast();
        return q2.removeFirst();
    }
    
    public int top() {
        return q2.peek();
    }
    
    public boolean empty() {
        return q1.size() == 0;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */