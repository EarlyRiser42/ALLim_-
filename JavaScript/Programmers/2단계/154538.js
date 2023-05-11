class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
        this.prev = null;

    }
}

class Deque {
    constructor() {
        this.init();
    }

    init() {
        this.count = 0;
        this.front = null;
        this.rear = null;
    }

    unshift(value) {
        const node = new Node(value);

        if (!this.front) {
            this.front = node;
            this.rear = node;
        } else {
            this.front.prev = node;
            node.next = this.front;
            this.front = node;
        }

        this.count += 1;
        return this.count;
    }

    shift() {
        if (this.count === 0) return null;

        const value = this.front.value;

        if (this.count === 1) {
            this.init();
        } else {
            this.front = this.front.next;
            this.front.prev = null;
            this.count -= 1;
        }

        return value;
    }

    push(value) {
        const node = new Node(value);

        if (this.count === 0) {
            this.front = node;
            this.rear = node;
        } else {
            this.rear.next = node;
            node.prev = this.rear;
            this.rear = node;
        }

        this.count += 1;

        return this.count;
    }

    pop() {
        if (this.count === 0) return;

        const value = this.rear.value;

        if (this.count === 1) {
            this.init();
        } else {
            this.rear = this.rear.prev;
            this.rear.next = null;
            this.count -= 1;
        }

        return value;
    }

    getValue(idx) {
        if (idx >= this.count) return;
        let node = this.front;

        for (let i=1; i<=idx; i++) {
            node = node.next;
        }

        return node.value;
    }

    get array() {
        let arr = [];
        let node = this.front;

        for (let i = 0; i < this.count; i++) {
            arr.push(node.value);
            node = node.next;
        }

        return arr;
    }

    get length() {
        return this.count;
    }
}

function BFS(x,y,n){
    let num = new Array(1000001).fill((0))
    num[x] = 1
    let queue = new Deque()
    queue.push(x)
    while(queue.length){
        let a = queue.shift()
        if (a+n <= y && !num[a+n]){
            num[a+n] = num[a]+1
            queue.push(a+n)
        }

        if (2*a <= y && !num[a*2]){
            num[2*a] = num[a]+1
            queue.push(2*a)
        }

        if (3*a <= y && !num[a*3]){
            num[3*a] = num[a]+1
            queue.push(3*a)
        }
    }
    return num[y]-1
}

function solution(x, y, n) {
    return BFS(x,y,n)
}