import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();
const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    }
];

before(() => queue.testMode.enter());
afterEach(() => queue.testMode.clear());
after(() => queue.testMode.exit());

it('create a new job', () => {
  createPushNotificationsJobs(jobs, queue);
  expect(queue.testMode.jobs.type).to.equal(Array);
});