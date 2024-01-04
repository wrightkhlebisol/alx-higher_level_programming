#!/usr/bin/node
const request = require('request');
const process = require('process');

const url = process.argv[2];
const totalCompleted = {};

request(`${url}?completed=true`, (err, res, body) => {
  if (err) {
    return console.error(err);
  }
  const completedTasks = JSON.parse(body);
  if (completedTasks.length) {
    completedTasks.forEach(completedTask => {
      totalCompleted[completedTask.userId]
        ? totalCompleted[completedTask.userId]++
        : totalCompleted[completedTask.userId] = 1;
    });
  }
  console.log(totalCompleted);
});
