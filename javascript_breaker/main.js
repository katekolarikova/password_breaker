// function sendStringToServer(stringToSend) {
//     var userInput = document.getElementById('user_input');
//     userInput.value = stringToSend;
//
//     var checkButton = document.getElementById('check_button');
//
//     var clickEvent = new MouseEvent('click', {
//         'view': window,
//         'bubbles': true,
//         'cancelable': true
//     });
//
//     checkButton.dispatchEvent(clickEvent);
// }
//
// // Replace 'YourDesiredString' with the desired string to send
// sendStringToServer('1234');
//

// function sendData() {
//     var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
//     const xhr = new XMLHttpRequest();
//     var url = 'http://127.0.0.1:4000/'; // Replace with your server URL
//
//     xhr.open('POST', url, true);
//     xhr.setRequestHeader('Content-Type', 'application/json');
//
//     xhr.onreadystatechange = function () {
//         if (xhr.readyState === XMLHttpRequest.DONE) {
//             if (xhr.status === 200) {
//                 // Request was successful
//                 console.log('Data sent successfully');
//             } else {
//                 // Handle errors
//                 console.error('Error:', xhr.status);
//             }
//         }
//     };
//
//     var data = JSON.stringify({ input: '1234' }); // Format your data as needed
//     xhr.send(data);
// }
//
// sendData();
// const fetch = require('node-fetch');
import { fetch, setGlobalDispatcher, Agent } from 'undici';

setGlobalDispatcher(new Agent({ connect: { timeout: 60_000 } }) );


// The data you want to send
const userInput = '004';

// URL of your Flask server
const url = 'http://127.0.0.1:5000/';

// Data to send in the POST request
const data = new URLSearchParams();
data.append('user_input', userInput);

const letters = [...'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']; // includes both uppercase and lowercase letters
const numbers = [...'0123456789'];
const specialCharacters = [...'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'];


function cartesianProduct(arrays) {
    return arrays.reduce((acc, array) => acc.flatMap(x => array.map(y => [...x, y])), [[]]);
}

const passwordStrength = {
    numbers: numbers,
    numbers_letters: [...numbers, ...letters],
    numbers_letters_special_characters: [...numbers, ...letters, ...specialCharacters]
};

// Generate combinations for the 'numbers' key, repeat=4 times
const level = cartesianProduct(Array.from({ length: 4 }, () => passwordStrength['numbers']));

let len = level.length;


// Generate combinations for the 'numbers' key, repeat=4 times

// Sending the POST request

for (let i=0; i<len; i++)
{
    let tmp = level[i].join('');
    const data = new URLSearchParams();
    data.append('user_input', tmp);
    fetch(url, {
        method: 'POST',
        body: data,
    })
        .then(response => {
            if (response.status==200) {
                console.log(response.status)
                console.log(tmp)
            }


            if (response.ok) {
                return response.text(); // or response.json(), depending on the response type
            }
            //throw new Error('Network response was not ok');
        })
        .then(data => {
            //console.log(data.status); // Process the response data here
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        })

}


