import { createClient } from 'redis';

const client = createClient();

client.connect();

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', err => console.log(`Redis client not connected to the server: ${err.message}`));

const schoolChannel = "holberton school channel";

client.subscribe(schoolChannel);

client.on('message', (channel, message) => {
  console.log(message);
  if (message === schoolChannel) {
    client.unsubscribe(schoolChannel);
    process.exit(0);
  }
});
