Q1. Describe how you could mix streaming computation with iterative computation.
Take calculating connected component of a graph as an example to demonstrate
your idea. You may assume that new graph nodes (e.g, new social network users)
and new edges (e.g, new social network friendships) are streaming into your
system. Show using an example how your mixture is able to compute connected
components over a streaming graph.

Hints: 

1. Try to extend the connected components calculation using the iterative label
exchange algorithm discussed during the winter school.
2. Try to use Popper's monotonic/non-monotonic and incremental/non-incremental
taxonomy of operators to see if you can extend the above iterative algorithm
into iterative + streaming algorithm.

Q2. For the streaming + iterative computation in Q1, describe an asynchronous
checkpointing mechanism that creates consistent checkpoints. Argue about its
correctness. Proof by example suffices.

Hint: Try to extend Flink's marker-based algorithm (Chandy-Lamport algorithm) we
discussed during the winter school. During the winter school, we showed how it
works for DAGs.

Q3. Try to extend the Q1's computation such that it can also handle streaming
retractions of graph nodes (e.g, deleted social network users) and of graph
edges (e.g, deleted social network edges).

Q4. Describe your experiences (provide link to your code if possible) with using
Popper in doing lab 4 or with some different use cases.