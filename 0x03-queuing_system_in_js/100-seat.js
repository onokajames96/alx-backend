import express from 'express';
import kue from 'kue';
import redis from 'redis';
import { promisify } from 'util';

// Redis setup
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

const seatsKey = 'available_seats';
const initialAvailableSeats = 50;
let reservationEnabled = true;

client.set(seatsKey, initialAvailableSeats);

// Kue setup
const queue = kue.createQueue();
const queueName = 'reserve_seat';

// setup
const app = express();
const port = 1245;

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});

function reserveSeat(number) {
  client.set(seatsKey, number);
}

async function getCurrentAvailableSeats() {
  const availableSeats = await getAsync(seatsKey);
  return parseInt(availableSeats);
}

// Routes
app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create(queueName).save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    return res.json({ status: 'Reservation in process' });
  });

  job.on('complete', (result) => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

app.get('/process', async (req, res) => {
  queue.process(queueName, async (job, done) => {
    try {
      let availableSeats = await getCurrentAvailableSeats();

      if (availableSeats <= 0) {
        throw new Error('Not enough seats available');
      }

      availableSeats--;
      reserveSeat(availableSeats);

      if (availableSeats <= 0) {
        reservationEnabled = false;
      }

      done();
    } catch (error) {
      done(error);
    }
  });

  res.json({ status: 'Queue processing' });
});
