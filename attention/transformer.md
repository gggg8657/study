# Attention is all you need

* Background
    * 기존 방식의 한계점
        - the number of OPs required to relate signals from two arbitary input or output positions grows **<- cause**
        - linearly for ConvS2S andd logarithmically for ByteNet. -> This Makes it more difficult to learn dependencies between distant positions. **<- effect** 
    * In the transformer
        - this is reduced to a **_constant number of operations,_** albeit at the cost of reduced dffective resolution due to **_averaging attention-wighted positions._**
    * key
        - **_Attention_** is a generalisation of the idea of **_weighting inputs by distance._**