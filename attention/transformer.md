# Attention is all you need

* Background
    * 기존 방식의 한계점
        - the number of OPs required to relate signals from two arbitary input or output positions grows **<- cause**
        - linearly for ConvS2S andd logarithmically for ByteNet. **->**This Makes it more difficult to learn dependencies between distant positions. **<- effect** 
    * In the transformer
        - this is reduced to a <span style='background-color: $ffdce0'>**_constant number of operations,_**</span> albeit at the cost of reduced dffective resolution due to <span style='background-color: $ffdce0'>**_averaging attention-wighted positions._**</span>
    * key
        - <span style='background-color: $ffdce0'>**_Attention_**</span> is a generalisation of the idea of <span style='background-color: $ffdce0'>**_weighting inputs by distance._**</span>
    * Self-attention (intra-attention)
        - is attention mechnism <span style='background-color: $ffdce0'>**_relating different positions of a sngle seq_**</span> in order to compute a _representation of the seq_
    * End-to-end memory networks
        - are memory networks that use <span style='background-color: $ffdce0'>**_attention_**</span> to compute a representation of the input sequence
        - based on recurrenct attention mechanism <span style='background-color: $ffdce0'>**_instead of seq-aligned recurrence_**</span>
* Model Architecture
    * Most competetive neural seq transduction models 
        - encoder : maps an input seq of symbol representations **_x_ = (_x~1_, _x~2_, ..., _x~n_)** to a sequence of continuous representations **_z_ = (_z~1_, _z~2_, ..., _z~n_)**
        - decoder : Given **_z_ = (_z~1_, _z~2_, ..., _z~n_)** generate an ouput seq **(_y~1_, _y~2_, ..., _y~n_)** of symbols **one element at ta time**