import { uploadPhoto, createUser } from './utils.js';

export default function handleProfileSignup() {
  const promisePhoto = uploadPhoto();
  const promiseUser = createUser();
  const promises = [promisePhoto, promiseUser];
  Promise.all(promises)
    .then((results) => {
      console.log(results[0].body, results[1].firstName, results[1].lastName);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}