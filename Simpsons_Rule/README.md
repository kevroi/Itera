# Simpson's Rule
Simpson's Rule numerically evaluates definite integrals in one dimension in a geometrically similar, but more accurate manner than the trapzium rule. The definite integral is computed as the 'area under the curve', by splitting this area into equal width strips. The strips are then paired adjacently, and the unique quadratic curve that passes through the 3 points of our function is found. The area under this quadratic can easily be computed.

`Simpsons.py` implements the [composite Simpson's rule](https://en.wikipedia.org/wiki/Simpson%27s_rule#Composite_Simpson's_rule):