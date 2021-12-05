# What are Voronoi cells?
They're pretty.
## Formal Definition
For a set of N points, {P<sub>1</sub>, P<sub>2</sub>, ..., P<sub>N</sub>}, in a metric space, X, with a distance function, d, the Voronoi Cell for the k<sup>th</sup> point, P<sub>k</sub>, is denoted V<sub>k</sub>. It is the set of all points in X whose distance to P<sub>k</sub> is less than its distance to any other point P<sub>j</sub>.

V<sub>k</sub> = {xϵX | d(x,P<sub>k</sub>) < d(x,P<sub>j</sub>) ∀ j ≠ k}

## 5-year olds' Definition
Poke a bunch of random dots in different colours onto this page.

Colour all the space close to the red dot red. Now do the same for yellow, green and all the other points. Careful - a red space means its closest dot is your red dot.

Now go outside and play.

# Results
Voronoi diagrams for 5, 10 and 50 cells (top to bottom) with centres uniformly distributed across the 800x800 plane. Euclidean distance was used as the metric.

<div class="row">
  <div class="column">
    <img src="./results/E5.png" alt="Euclidean Distance Voronoi Diagram 5 cells" width="200" height="200">
  </div>
  <div class="column">
    <img src="./results/E10.png" alt="Euclidean Distance Voronoi Diagram 10 cells" width="200" height="200">
  </div>
  <div class="column">
    <img src="./results/E50.png" alt="Euclidean Distance Voronoi Diagram 50 cells" width="200" height="200">
  </div>
</div>


<!-- <img src="./results/E10.png" alt="Euclidean Distance Voronoi Diagram 10 cells" width="200" height="200">
![Euclidean Distance Voronoi Diagram 5 cells](./results/E5.png | width=100)
![Euclidean Distance Voronoi Diagram 10 cells](./results/E10.png)
![Euclidean Distance Voronoi Diagram 50 cells](./results/E50.png) -->

If we have a gaussian distribution of centres:
<img src="./results/E50G.png" alt="Euclidean Distance Gausian Voronoi Diagram 50 cells" width="200" height="200">
![Euclidean Distance Gausian Voronoi Diagram 50 cells](./results/E50G.png)

If we use Manhattan distance as the metric, with 25 cells:
<img src="./results/M25.png" alt="Manhattan Distance Voronoi Diagram 50 cells" width="200" height="200">

# Future Work
* Rectangular plots to generate wallpapers
* Maybe a heuristic method to determine nearest P<sub>k</sub> to a given pixel?