# Map-reduce style computation

In this lab, we will build a distributed word count application. But for
simplicity, we will pretend that our multi-core system is a distributed system
in itself.

We will start stateless python processes to act as distributed workers. These
workers will co-ordinate with each other through [Redis](https://redis.io/).
Redis behaves like the master (or driver program) in contemporary systems.  For
further simplicity, we do not create control plane/data plane separation which
is crucial for performance! Workers take tasks from Redis and push word counts 
back to Redis.

All workers have access to a shared file system for reading and writing large
inputs. This is again trivially true on our single system. In a real setup,
workers would additionally use a distributed file system like HDFS or a blob
store like S3.

## Lab instructions
You will use Python, Pandas and Redis for this Lab. 

Download the [starter code](./starter_code.zip)

Create a working directory and navigate to it:
   ```bash
   mkdir -p ws24/lab1 && cd ws24/lab1
   ```
Unzip the starter code into the working directory:
   ```bash
   unzip ../starter_code.zip
   ```

Note: Adjust the path to `starter_code.zip` based on where you downloaded the file.


Create a [`conda`](https://docs.anaconda.com/miniconda/install/#quick-command-line-install) environment with python 3.10 and install the required packages.


```bash
conda create -n lab1 python=3.10 && conda activate lab1 
```

Install the required packages inside the conda environment. The `requirements.txt` file is in the starter code.

```bash
pip install -r requirements.txt
```

### Redis Installation:

```bash
$ docker run -d -p 6379:6379 --name redis --rm redis:7.4
```

- Use the following commands to verify the successful installation of Redis.

```bash
$ redis-cli --version

#check if you got the right redis-server version
$ redis-cli -h 127.0.0.1 -p 6379 INFO server

$ redis-cli ping
```
### Running the code

Once you are done with the implementation/TODOs, run the `client.py` file to start the word count application.

```bash
python client.py
```
Download [RedisInsight](https://redis.com/redis-enterprise/redis-insight/) to visualize the Redis streams and sorted sets for better understanding.

### Dataset Description

The dataset is available at [link](https://www.kaggle.com/thoughtvector/customer-support-on-twitter). Each CSV file contains 7 attributes, following are a brief description of each attribute:

- **_tweet_id:_** A unique, anonymized ID for the Tweet. Referenced by response_tweet_id and in_response_to_tweet_id.
- **_author_id:_** A unique, anonymized user ID. [@s](https://www.kaggle.com/s) in the dataset have been replaced with their associated anonymized user ID.
- **_inbound:_** Whether the tweet is "inbound" to a company doing customer support on Twitter. This feature is useful when re-organizing data for training conversational models.
- **_created_at:_** Date and time when the tweet was sent.
- **_text:_** Tweet content. Sensitive information like phone numbers and email addresses are replaced with mask values like \__email_\_.
- **_response_tweet_id:_** IDs of tweets that are responses to this tweet, comma separated.
- **_in_response_to_tweet_id:_** ID of the tweet this tweet is in response to, if any.

### Problem Statement

**Count the occurrence of each word given a set of files**. Your task is to create an application that can handle the large amount of data, which is estimated to be in the range of GBs.

- Since a serial word count will not be sufficient, you need to design a scalable word count application that can handle the size of the dataset.
- Since there is a possibility of faults in the system, you need to make your implementation tolerant to worker faults (failures) as well as redis-server faults.

## Overview

- You are provided with the starter code for the challenge.
- Please use python version 3.10 and Redis version 7.4.
- A serial version of the word count code is provided as
[`serial.py`](./serial.py) for your reference. You can use this to evaluate the
correctness of your parallel implementation. Note that you just need to split
the text by the space delimiter to get the words.
- You can use the provided [`split_csv.py`](./split_csv.py) to split the dataset
into multiple small csv files.
- You can use the docker commands to restart redis. `docker stop redis`, `docker restart redis`.
- Evaluate your application by randomly killing your workers and by restarting
Redis.

## Part 0

Hope you already have Redis running. Familiarize yourself with [Redis](./redis). 
Learn sending commands to redis using `redis-cli` and from python programs using
the [redis-py](https://github.com/redis/redis-py) library. Especially
familiarize yourself with [sorted sets](https://redis.io/commands/zadd/). You
will use them to maintain word counts. You should also read about [redis
streams](https://redis.io/docs/data-types/streams-tutorial/). You need the
following redis stream commands for the first part: `xadd`, `xreadgroup`,
`xcreate_group` and `xack`. Understand what they do. Finally, you will need to
write a Redis function for making your tasks idempotent.


## Part 1: Parallel execution

We will first make the word count application run end-to-end using Redis.  But
before that, download the [starter code](./starter_code.zip).

Update `DATA_PATH` in `config.json` to point to your `data` folder.  Run 
`python3 client.py`. In this lab, you have to modify `worker.py` and `myrds.py`.

The basic structure is as follows: 

* `client.py` iterates over the folder with the text files to add the file paths
  into a redis stream using `xadd`. It then starts the worker processes.
* Worker processes do `xreadgroup` to read one file name from the Redis stream.
  Call `xreadgroup` such that each worker gets a different file name.
* Worker process reads the file it is supposed to work on and counts
  each word's frequency. 
* When done, the worker process can use `zincrby` to increment each word's count
  in a redis sorted set. And finally `xack` the message containing the filename.
* Then it reads another file by again calling `xreadgroup`. If there are no 
  more files to process, it exits.

## Part 2: Fault tolerance of workers

Now we wish to ensure that our system is tolerant to worker failures. Since,
workers are stateless, we should be ok with losing worker state. But, we still
have to ensure two things:

* Updates to redis should be made atomic. If a worker crashes after incrementing
  counts of only a few words, then we will end up with incorrect counts. See
  [Redis fcall](https://redis.io/commands/fcall/) to `xack` a file and to
  increment word counts as one atomic operation.
* Consumer groups in Redis streams ensure that each worker gets a unique file 
  name. But, if a worker crashes after getting a file name from Redis stream, 
  that file's words may never get counted. Therefore, other workers will 
  have to steal filenames that have not been `xack`ed till a timeout.
  See [xautoclaim](https://redis.io/commands/xautoclaim/) to do so.

> * You may add crash points in the worker process to control where and how
>   workers crash. For instance, after the worker reads a filename from
>   `xreadgroup`, it may call `sys.exit()` if a certain worker flag is set. 
>   Configure different flags for different workers at the time of their creation 
>   to verify fault tolerance.
> * Workers can not exit until all the other workers are done with their files.
>   Use [xpending](https://redis.io/commands/xpending/) to verify this before 
>   exiting from workers.
> * `xack` returns the number of Redis stream messages that were actually
>   acknowledged. Verify that `xack` returns 1 before writing to the word count
>   sorted set to get idempotence.

## Part 3: Redis FT using checkpoints

We would like to now ensure that our system tolerates Redis failures. We
need not change the worker code for this part. To reason about correctness, note
that a Redis instance handles one command after another in a single thread.

In this part, we will periodically create a checkpoint using
the [BGSAVE](https://redis.io/docs/management/persistence/#snapshotting)
command. Redis starts periodically storing a `dump.rdb` file on disk.

You can run `CONFIG GET dir` from `redis-cli` to find the directory where
`dump.rdb` gets stored. You may try to crash the Redis instance and then start a
new Redis instance. Redis should automatically read `dump.rdb` file and restore
from it. Verify that this new instance have the keys from the old instance by 
running `keys *` using `redis-cli`.

Now while the job is running, try crashing the Redis instance and restarting
another one. From a correctness standpoint, checkpoints are consistent because
Redis has a single event loop and because all our edits were made atomic in the
previous part. 

In other words, let us say that a file `foo` was processed after the checkpoint.
Now after a failover, the new Redis instance (recovered from the checkpoint)
will remember that the file has NOT yet been `xack`ed. Therefore, a worker will
again receive the file for processing and it will again `xack` + increment word
counts in one atomic operation. Since our workers are stateless and file counts 
are deterministic, recomputing a file's word counts are ok.

You can load the lua function `mylib.lua` into the Redis instance using the
following command:

```bash
cat mylib.lua | redis-cli -x FUNCTION LOAD REPLACE
```

> Ensure that you set up the new instance in an identical manner, i.e, listen on 
> the same port, set up the same password, and insert the same lua functions.
