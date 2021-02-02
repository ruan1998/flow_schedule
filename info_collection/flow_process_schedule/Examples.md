## 仿真示例一
```mermaid
flowchart LR
id1((1))
id2((2))
id3((3))
id4((4))
id5((5))
id6((6))
id7((7))
id8((8))
id9((9))

id1 --> id2 --> id5 --> id4
id1 --> id3 --> id4
id2 --> id7
id3 --> id5
id8 --> id5 & id6 & id9
id4 --> id8 
id3 --> id7 --> id9
id6 --> id9
id5 --> id6  --> id2
```

- 初始状态 1 6 （60%， 40%）
- 状态转移矩阵
- 约束、终止条件
	- 到达末端节点9
	- 最长时间T：10

````gfm
```flow
st=>start: Start
op=>operation: Your Operation
cond=>condition: Yes or No?
e=>end

st->op->cond
cond(yes)->e
cond(no)->op
````