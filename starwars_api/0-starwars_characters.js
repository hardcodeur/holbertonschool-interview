#!/usr/bin/node
const process = require('process');
const request = require('request');

if (process.argv < 2) throw new Error('Empty argument add the number of movie');

const filmArg = parseInt(process.argv[2], 10);

if (!filmArg) throw new Error('The argument should be a star wars film number');
if (filmArg > 7) throw new Error('Invalide number, the number should be between 1 and 7');

const apiUrl = `https://swapi-api.hbtn.io/api/films/${filmArg}`;

const getCharacterName = async (characterUrl) => {
  return new Promise((resolve, reject) => {
    request.get(characterUrl, function (error, response, body) {
      if (error) {
        reject(error);
      } else if (response.statusCode === 200) {
        const data = JSON.parse(body);
        resolve(data.name);
      } else {
        reject(response.statusCode);
      }
    });
  });
};

request.get(apiUrl, async (error, response, body) => {
  if (error) {
    Error(error);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    for (let index = 0; index < data.characters.length; index++) {
      console.log(await getCharacterName(data.characters[index]));
    }
  } else {
    Error(`Error : ${response.statusCode}`);
  }
});
