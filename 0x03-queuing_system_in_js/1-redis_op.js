import { createClient } from 'redis';

const client = createClient();

client.connect();

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', err => console.log(`Redis client not connected to the server: ${err.message}`));


const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, (err, replay) => {
    console.log(`Replay: ${replay}`);
  });
}

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, replay) => {
    console.log(replay);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');