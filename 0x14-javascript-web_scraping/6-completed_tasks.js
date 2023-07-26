#!/usr/bin/node
// Create an object to store the completed task count for each user ID.

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const tasks = JSON.parse(body);

    // Create an object to store the completed task count for each user ID.
    const completedTasksByUser = {};

    // Loop through the tasks and count completed tasks for each user.
    for (const task of tasks) {
      if (task.completed) {
        const userId = task.userId;
        completedTasksByUser[userId] = (completedTasksByUser[userId] || 0) + 1;
      }
    }

    console.log(completedTasksByUser);
  }
});
