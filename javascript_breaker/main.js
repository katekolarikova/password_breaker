import { fetch, setGlobalDispatcher, Agent } from 'undici';
// setGlobalDispatcher(new Agent({ connect: { timeout: 60_000 } }) );

// URL of your Flask server
const url = 'http://127.0.0.1:5000/';

// Generate all possible characters for password level
const letters = [...'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'];
const numbers = [...'0123456789'];
const specialCharacters = [...'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'];
const passwordStrength = {
    numbers: numbers,
    letters: letters,
    numbers_letters: [...numbers, ...letters],
    numbers_letters_special_characters: [...numbers, ...letters, ...specialCharacters]
};

// Define password level
const repeat = 4;
let to_use = passwordStrength['numbers_letters'];
let totalCombinations = Math.pow(to_use.length, repeat);

// Sending the POST request
let startTime = new Date();
for (let i=0; i< totalCombinations; i++) {

    // Generate password
    const variation = [];
    let index = i;
    for (let j = 0; j < repeat; j++) {
        const arrIndex = index % to_use.length;
        variation.push(to_use[arrIndex]);
        index = Math.floor(index / to_use.length);
    }
    let tmp = variation.join('');

    // Send POST request
    const data = new URLSearchParams();
    data.append('user_input', tmp);
    await fetch(url, {
        method: 'POST',
        body: data,
    })
        .then(response => { // Check if the password is correct
            if (response.status==200) {
                console.log(response.status)
                console.log("Password: "+tmp)
                totalCombinations=0; // Stop the loop
            }
            if (response.ok) {
                return response.text();
            }
        })
        // .then(data => {
        //     //console.log(data.status);
        // })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        })
}
let endTime = new Date();
let timeElapsed = endTime - startTime;
console.log("Time elapsed: "+timeElapsed/1000+" seconds");