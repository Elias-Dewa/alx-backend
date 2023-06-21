import { createClient } from 'redis';
import { promisify} from 'util';

const client = createClient();

client.connect();

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', err => console.log(`Redis client not connected to the server: ${err.message}`));


const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, (err, replay) => {
    console.log(`Replay: ${replay}`);
  });
}

const displaySchoolValue = async (schoolName) => {
  const asyncGet = promisify(client.get).bind(client);
  const replay = await asyncGet(schoolName)
  console.log(replay);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');