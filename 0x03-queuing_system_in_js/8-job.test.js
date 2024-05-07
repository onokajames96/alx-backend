import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue({ redis: { port: 6379, host: '127.0.0.1' } });
queue.testMode.enter();

describe('createPushNotificationsJobs', () => {
    after(() => {
        queue.testMode.exit();
    });

    it('should display an error message if jobs is not an array', () => {
        expect(() => createPushNotificationsJobs(null, queue)).to.throw('Jobs is not an array');
    });

    it('should create new jobs in the queue', () => {
        const list = [
            {
                phoneNumber: '4153518780',
                message: 'This is the code 1234 to verify your account'
            },
            {
                phoneNumber: '1234567890',
                message: 'Your order has been dispatched'
            }
        ];

        createPushNotificationsJobs(list, queue);

        const jobs = queue.testMode.jobs;
        expect(jobs).to.have.lengthOf(list.length);

        jobs.forEach((job, index) => {
            const jobData = list[index];
            expect(job.type).to.equal('push_notification_code_3');
            expect(job.data).to.deep.equal(jobData);
        });
    });
});
