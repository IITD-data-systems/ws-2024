# Winter School 2024 on Data Systems

[Welcome](#about) | [Registration](#registration)  | [Logistics](#logistics) | [Schedule](#schedule) | [Program](#program)

> [!IMPORTANT]  
> Selected candidates have already been notified via email. All selected
candidates are kindly requested to join the Google group
https://groups.google.com/g/ds-ws24 for the latest updates and communications.
An invitation has also been sent; if you have not received it, please check your
spam folder. 

## Welcome<a name="about"></a>
The **Winter School 2024 on Data Systems**, organized by the Data Systems Group
of the [Department of Computer Science and
Engineering](https://www.cse.iitd.ac.in/) at IIT Delhi, will be held from
**December 2nd to December 6th, 2024**. Supported by the Mohit Aron Endowment,
this winter school provides an exceptional opportunity for final-year
undergraduate students, master’s and PhD students, and industry professionals to
deepen their knowledge in **scalable systems for Big Data, Data Science and
AI**. 

Participants will engage in lectures and hands-on lab sessions on a range of
data systems topics, led by [Prof. Kaustubh
Beedkar](https://web.iitd.ac.in/~kbeedkar) and [Prof. Abhilash
Jindal](https://abhilash-jindal.com/). 

## Registration <a name="registration"></a>
Applications are open to final-year undergraduate students, master’s and PhD
students, and industry professionals with an interest in scalable systems for
Big Data, Data Science, and AI. The application process for Winter School 2024
consists of two rounds:

1. **First Round - Application Submission**  
   Interested candidates must submit their applications via the provided [online
   form](https://forms.gle/yFiBrePKKWymrybg7) by **5:00 pm on 14th November
   2024**. Only candidates who complete this submission will be considered for
   the next round.
   
2. **Second Round - Online Test**  
   Candidates who have successfully applied in the first round will be invited
   to participate in an online test scheduled for ~~16th November 2024~~ **17th
   November 2024 at 10:00 AM**.
   
Selected candidates will receive notification of their acceptance into the
Winter School by ~~17th November 2024~~ **21st November 2024**.

## Logistics<a name="logistics"></a>
- **Venue**: Department of Computer Science and Engineering, IIT Delhi
- **Dates**: December 2nd – December 6th, 2024
- **Accommodation**: Hostel accommodation including breakfast, lunch, dinner,
and high tea will be provided from Dec 1st -- Dec 7th, 2024. In addition, a
stipend of 2000 INR will be provided to selected students. Participants will be
required to check in on December 1st, 2024, and check out before noon on
December 7th, 2024.
- **After winter school**: Participants who successfully complete the Winter
School will receive a **Certificate of Participation**. *Please note that we
will not provide recommendation letters for graduate school applications.*
Students will be encouraged to apply for paid internships at IIT Delhi during
the 8 weeks of summer 2025.

## Daily Schedule <a name="schedule"></a>
| Time                | Activity                                                |
| ------------------- | ------------------------------------------------------- |
| 09:00 am – 10:15 am | Lecture                                                 |
| 10:15 am – 10:45 am | Break + high tea with instructors + offline discussions |
| 10:45 am – 01:00 pm | Lectures with appropriate breaks                        |
| 01:00 pm – 02:00 pm | Lunch Break                                             |
| 02:00 pm – 05:00 pm | Lab                                                     |
| 03:30 pm – 04:00 pm | High tea                                                |


## Program <a name="program"></a>
The Winter School will cover the following topics:

### Day 1: Distributed data processing
* Holy grail: transparently scale, and tolerate faults/stragglers;
* Difficulties in transparent locality, scalability, fault tolerance, and
straggler mitigation;
* Introduction to checkpointing and replication;
* Introduction to distributed data processing with MapReduce;
* Main ideas: functional programming model; separate control and data plane;
locality optimizations, re-execute lost/backup tasks, deterministic/idempotent
tasks.
* Lab: Write a fault tolerant computation from scratch

### Day 2: Dataflow systems for batch processing
* *Keynote address: TBA*
* Spark's Resilient distributed dataset (RDD) abstraction: write-once for
consistent replication, coarse-grained transformations to reduce lineage,
lineage-based re-execution of lost/backup tasks;
* Abstractions beyond MapReduce, lazy execution, stage planning, narrow
and wide-dependencies, query optimizations.
* Lab: Hands-on exercises with Spark.

### Day 3: Dataflow systems for stream processing
* Semantics of stream processing: unbounded streams, event time vs processing
time, hopping/sliding/session windows, watermarks;
* Streaming query optimizations and continuous operator model of Flink for
low-latency;
* Fault tolerance: problems due to state in continuous operators, pull state
out of operators by discretizing streams, consistent checkpoints in Flink using
Chandy-Lamport algorithm.
* Lab: Hands-on exercises with Flink.


### Day 4: Cyclic dataflow systems
* Iterative data processing: solving graph problems with iterative data
processing, driver-based iterations vs native iterations with cyclic dataflows,
changes for creating consistent checkpoints.
* Introduction to ML workflows: error handling and correction as a first class
citizen, Reactive dataflow with deletes, edits, and appends.
* Backward and forward lineage for backward tracing and delete propagation, 
stage planning with incremental/non-incremental, monotonic/non-monotonic
operators
* Lab: Hands-on exercises with Popper.

### Day 5: Cross-platform data processing
* Introduction to Wayang: a platform for cross-framework data processing,
allowing optimizations across Spark, Flink, and Relational Databases.
* Sessions about data systems research at IITD, guiding participants interested
in pursuing higher studies, and research success stories.
* Lab: Hands-on exercises with Wayang.

> Disclaimer: The schedule and topics are only tentative. They are subject to
change depending upon attendee interests.