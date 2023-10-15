# Attention is all you need

* Background
    * 기존 방식의 한계점
        - the number of OPs required to relate signals from two arbitary input or output positions grows **<- cause**
        - linearly for ConvS2S andd logarithmically for ByteNet. This Makes it more difficult to learn dependencies between distant positions. **<- effect** 
    * In the transformer
        - this is reduced to a **_constant number of operations,_**</span> albeit at the cost of reduced dffective resolution due to <span style='background-color: $ffdce0'>**_averaging attention-wighted positions._**
    * key
        - **_Attention_** is a generalisation of the idea of **_weighting inputs by distance._**
    * Self-attention (intra-attention)
        - is attention mechnism **_relating different positions of a sngle seq_** in order to compute a _representation of the seq_
    * End-to-end memory networks
        - are memory networks that use **_attention_** to compute a representation of the input sequence
        - based on recurrenct attention mechanism **_instead of seq-aligned recurrence_**
* Model Architecture
    * Most competetive neural seq transduction models 
        - encoder : maps an input seq of symbol representations **_x_ = (_x<sub>1_, _x<sub>2_, ..., _x<sub>n_)** to a sequence of continuous representations **_z_ = (_z<sub>1_, _z<sub>2_, ..., _z<sub>n_)**
        - decoder : Given **_z_ = (_z<sub>1_, _z<sub>2_, ..., _z<sub>n_)** generate an ouput seq **(_y<sub>1_, _y<sub>2_, ..., _y<sub>n_)** of symbols **one element at ta time**, consuming the previously generated symbols as additional input when generating the next.
    * **_Transformer follows this overall architecture using stacked slf-attention and pointwise, FC layers for both the encoder and decoder, shown in the left and right halves of picutre respectively_**
        
        ![screensh](https://jalammar.github.io/images/t/transformer_resideual_layer_norm_3.png)
        출처 : https://jalammar.github.io/illustrated-transformer/
* Encoder
    * 