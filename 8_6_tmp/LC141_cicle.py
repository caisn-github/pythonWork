### 这个是LC141,用来解决在链表中是否存在环形链表的

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def hasCycle(head:ListNode) -> bool:
    ## 假设现在只知道一个头的情况下，似乎没有办法用长度这种来做，假设是有长度的话，完全可以遍历2N次，看是否遍历到空
    ## 但是因为现在假设只知道一个链表的头，那么就需要用快慢链表来做了
    quick = head
    if quick == None:
        return False
    if quick.next == None:
        return False 
    if quick.next == quick:
        return True 

    ## 接下来是一些最常见的情况：
    low = quick
    quick = quick.next
    while low and quick:
        if low == quick: ## 注意不能用val来判断，val不代表这个节点
            return True
        low = low.next # 因为low一定在quick后面，所以low不用判断
        if quick.next == None:
            return False
        quick = quick.next
        if quick.next == None:
            return False
        quick = quick.next
        ## 快的一次跑两格，慢的一次跑一格，假设相遇，就一定能遇到

    return False



if __name__ == "__main__":
    circle = [3,2,0,-4]
    pos = 1
    
    head = ListNode(circle[0]) 
    cur = head
    for i in range(1,len(circle)):
        cur.next = ListNode(circle[i])
        cur = cur.next

    tmp = head
    i = 0
    if pos == -1:
        cur.next = None
    else:
        while tmp.next:
            if i == pos:
                cur.next = tmp
                break
            i += 1

    if_circle = hasCycle(head)

    print(if_circle)