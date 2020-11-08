# Note

本周主要学习了一些基础知识，如时间复杂度和空间复杂度。学习了一些数据结构，一维：**数组(Array), 链表(linked list)，二维：栈(stack), 队列(queue)，双端队列(deque)**。并进行了相关题目的练习。

### 部分题目思路记录：

#### 1. 2sum

两层循环遍历

哈希表

#### 283. 移动零

- loop, count zeros
- 开新数组，loop
- index
- 双指针

#### 206. 反转链表](https://leetcode-cn.com/problems/reverse-linked-list/)

- 首先 pre 指针指向 Null，cur 指针指向 head；

- 当 cur != Null，执行循环。

  - 先将 cur.next 保存在 temp 中防止链表丢失：temp = cur.next

  - 接着把 cur.next 指向前驱节点 pre：cur.next = pre
  - 然后将 pre 往后移一位也就是移到当前 cur 的位置：pre = cur
  - 最后把 cur 也往后移一位也就是 temp 的位置：cur = temp

- 当 cur == Null，结束循环，返回 pre。

![image-20200627220535158.png](E:\2018Summer\master_degree\小论文\result_pic\039a6eff23111dba77d91ed909bbd35539b1185c07664372b129216a7b779b4a-image-20200627220535158.png)

#### 24. 两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)

Here, `pre` is the previous node. Since the head doesn't have a previous node, I just use `self` instead. Again, `a` is the current node and `b` is the next node.

To go from `pre -> a -> b -> b.next` to `pre -> b -> a -> b.next`, we need to change those three references. Instead of thinking about in what order I change them, I just change all three at once.

