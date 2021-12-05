# What are Voronoi cells?
They're pretty.
## Formal Definition
For a set of N points, {P<sub>1</sub>, P<sub>2</sub>, ..., P<sub>N</sub>}, in a metric space, X, with a distance function, d, the Voronoi Cell for the k<sup>th</sup> point, P<sub>k</sub>, is denoted V<sub>k</sub>. It is the set of all points in X whose distance to P<sub>k</sub> is less than its distance to any other point P<sub>j</sub>.

V<sub>k</sub> = {xϵX | d(x,P<sub>k</sub>) < d(x,P<sub>j</sub>) ∀ j ≠ k}

## 5-year olds' Definition
Poke a bunch of random dots in different colours onto this page.

Colour all the space close to the red dot red. Now do the same for yellow, green and all the other points. Careful - a red space means its closest dot is your red dot.

Now go outside and play.

# Future Work
Maybe a heuristic method to determine nearest P<sub>k</sub> to a given pixel?