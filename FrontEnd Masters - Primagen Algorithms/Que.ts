// First in First out
// Last in Last out

// A > B > C > D
// Head >>>>> Tail
// to add have tail point to new. this.tail.next = E
// this.tail = E
// to pop Head is now pointed to B, remove link to current Head
// head = head.next
// head.next = null

type Node<T> = {
    value: T,
    next?: Node<T>,
}
export default class Queue<T> {
    public length: number;
    private head?: Node<T>;
    private tail?: Node<T>;

    constructor() {
        this.head = this.tail = undefined
        this.length = 0
    }

    enqueue(item: T): void {
        const node = {value:item} as Node<T>
        this.length++
        if (!this.tail){
            this.tail = this.head = node
            return
        }
        this.tail.next = node
        this.tail = node
    }
    deque(): T | undefined {
        if (!this.head){
            return undefined
        }
        this.length--
        const head = this.head
        this.head = this.head.next

        //free memory
        head.next = undefined
        return head.value
    }
    peek(): T | undefined {
        return this.head?.value
    }

}