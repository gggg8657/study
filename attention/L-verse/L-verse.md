# L-verse

* Related Work
    * VQ-VAE
    * Image - to - text Generation
    * Text - to - Image Generation

* Method
    * Preliminary
        * Stage 1 : Train a discrete VAE to compress each 256 X 256 RGB into a 32 X 32 grid of image tokens with each element of 8192(d<sub>z</sub>) possible values.
        * Stage 2 : Concatenate up to 256BPE-encoded text tokens with the 32 X 32= 1024 image tokens, and train an auto-regressive transformer to model the joint distribution over text and image tokens.
        