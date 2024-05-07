# 0x03 Queuing System in JS
This project is focused on building a queuing system in JavaScript using Redis, Node.js, and Express.js. By the end of this project, you'll gain knowledge about running a Redis server, interacting with Redis using Node.js, implementing a queue system with Kue, and building a basic Express application that interacts with Redis and a queue.

# Installation
To set up and run this project, follow these steps:

# Install Redis
Download the latest stable Redis version from redis.io.
Extract and compile Redis:

$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make
# Start Redis Server
Run Redis server in the background:

$ src/redis-server &
# Set up Redis Client
Ensure the Redis client is working:

$ src/redis-cli ping
PONG

# Clone Repository
Clone the project repository:
bash

$ git clone https://github.com/alx-backend/0x03-queuing_system_in_js.git
$ cd 0x03-queuing_system_in_js
 
#Install Dependencies
Install project dependencies using npm:
bash

- $ npm install
Usage
- Task 0: Install a Redis instance
Make sure to have Redis installed and running as per the instructions above.
Copy dump.rdb from the Redis installation directory (redis-5.0.7) to the root of the project.
- Task 1: Node Redis Client
Create a Redis client script 0-redis_client.js using ES6 and Babel.
Run the script to connect to the Redis server and verify the connection.
- Task 2: Node Redis Client and Basic Operations
Implement basic Redis operations (set, get) using callbacks.
Create a script 1-redis_op.js for these operations.
- Task 3: Node Redis Client and Async Operations
Refactor the operations from 1-redis_op.js to use promisify and async/await.
Create a script 2-redis_op_async.js to demonstrate async operations.
- Task 4: Node Redis Client and Advanced Operations
Use Redis to store hash values (hset and hgetall).
Implement hash operations in 4-redis_advanced_op.js.
- Task 5: Node Redis Client Publisher and Subscriber
Create scripts 5-subscriber.js and 5-publisher.js to demonstrate Redis pub/sub functionality.
- Task 6: Create the Job Creator
Implement job creation using Kue in 6-job_creator.js.
- Task 7: Create the Job Processor
Implement job processing using Kue in 6-job_processor.js.
- Task 8: Track Progress and Errors with Kue (Job Creator)
Create job creation tasks using Kue in 7-job_creator.js.
- Task 9: Track Progress and Errors with Kue (Job Processor)
Create job processing tasks with error handling using Kue in 7-job_processor.js.
- Task 10: Writing the Job Creation Function
Create a function to generate Kue jobs for push notifications in 8-job.js.
- Task 11: Writing the Test for Job Creation
Write tests using Mocha to validate job creation in 8-job.test.js.
- Task 12: In Stock?
Implement an Express server for managing product inventory with Redis integration in 9-stock.js.
Project Structure
The project directory structure will be organized as follows:

# Structure of the project
0x03-queuing_system_in_js/
├── 0-redis_client.js
├── 1-redis_op.js
├── 2-redis_op_async.js
├── 4-redis_advanced_op.js
├── 5-subscriber.js
├── 5-publisher.js
├── 6-job_creator.js
├── 6-job_processor.js
├── 7-job_creator.js
├── 7-job_processor.js
├── 8-job.js
├── 8-job-main.js
├── 8-job.test.js
└── 9-stock.js
Requirements
. Ubuntu 18.04
. Node.js 12.x
. Redis 5.0.7
. Getting Started
To begin the project, make sure you have Redis installed and configured as per the instructions above. Then, clone the repository, install dependencies, and proceed to run each task script using npm run dev <script_name.js>.

Note: The project will be executed using nodemon and babel-node for ES6 support.

Manual QA Review
Once the project tasks are completed, please request a manual QA review for validation and feedback.

