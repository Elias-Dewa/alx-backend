import { createClient, print } from 'redis';

const client = createClient();

client.connect();

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', err => console.log(`Redis client not connected to the server: ${err.message}`));

const school = "HolbertonSchools";
const values = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2
}

for (const [key, value] of Object.entries(values)) {
  client.hSet(school, key, value, (err, replay) => redis.print(`Replay: ${replay}`));
}

client.hGetAll(school, (err, object) => console.log(object));