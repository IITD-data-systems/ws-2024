## Summer internships 2025

Below are some open questions related to our research in the Data Systems lab
that we encourage you to explore. If you're interested in a summer internship,
we invite you to try solving one or more of these problems and share your
insights with us.


### Streaming and Iterative Computations
- Q1. Describe how you could mix streaming computation with iterative computation.
  Take calculating connected components of a graph as an example to demonstrate
  your idea. You may assume that new graph nodes (e.g., new social network users)
  and new graph edges (e.g., new social network friendships) are streaming into your
  system. Using an example, show how your mixture can compute connected
  components over a streaming graph.
  
  *Hints:* 
  1. Try to extend the connected components calculation using the iterative label
  exchange algorithm discussed during the winter school.
  2. Try to use Popper's monotonic/non-monotonic and incremental/non-incremental
  taxonomy of operators to see if you can extend the above iterative algorithm
  into iterative + streaming algorithm.

- Q2. For the streaming + iterative computation in Q1, describe an asynchronous
  checkpointing mechanism that creates consistent checkpoints. Argue about its
  correctness. Proof by example suffices.
  
  *Hint:* Try to extend Flink's marker-based algorithm (Chandy-Lamport algorithm) we
  discussed during the winter school. During the winter school, we showed how it
  works for DAGs.

- Q3. Try to extend the Q1's computation such that it can also handle streaming
retractions of graph nodes (e.g, deleted social network users) and of graph
edges (e.g, deleted social network friendships).

---

### Popper
- Describe your experiences (provide your code if possible) with using Popper
with use cases discussed in lab 4 or with some different use cases.
- Read the following paper: [Reactive Dataflow for Inflight Error Handling in ML
Workflows](http://abhilash-jindal.com/assets/pdfs/deem24.pdf). Identify one or
more limitations and propose how you would overcome those limitations. Include a
proof-of-sketch solution to the problems you identify.


---

### Compliant Data Systems
- Read the following papers: [Compliant Geo-distributed Query Procesing](https://web.iitd.ac.in/~kbeedkar/publication/cqp-sigmod-21/) and [Disclosure-compliant Query Answering](https://web.iitd.ac.in/~kbeedkar/publication/dcqa-sigmod-25/). Identify one or more limitations in each and propose how you would overcome those limitations. Include a proof-of-sketch solution to the problems you identify.

---

### Federated Data Discovery
 - Read the [Fainder paper](https://web.iitd.ac.in/~kbeedkar/publication/fainder-vldb-24/) that proposes how to leverage histograms from federated data repositories to support distribution-aware dataset search. One limitation of Fainder is that it only supports one-sided ranges. For example, it can search for datasets where 30% of the population is below the age of 50. How would you go about developing an index that natively supports two-sided ranges? For instance, when searching for datasets where 30% of the population is below the age of 50 and over the age of 20.
    
 - Read about some other approximate data summary structures such as the [Count-Min sketch](https://en.wikipedia.org/wiki/Count%E2%80%93min_sketch) and [HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog). Think of how they can be used in a federated setting for data discovery. What kind of dataset search queries could one do assuming these summaries about the datasets are available?

---

### Apache Wayang
- Download and install [Apache Wayang](https://wayang.apache.org/) locally on your laptops. Try out the exercise in lab 2 using Wayang. Provide a link to your (GitHub) code.

- How will you add a new data source in Wayang? For example, try adding support for MongoDB so that using Wayang, one can easily read data from MongoDB and process it on Spark. Provide a link to your (GitHub) code. 

