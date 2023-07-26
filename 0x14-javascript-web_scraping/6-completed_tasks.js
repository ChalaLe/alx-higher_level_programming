#!/usr/bin/node
const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

function fetchTasks() {
  return new Promise((resolve, reject) => {
    request(apiUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const tasks = JSON.parse(body);
        resolve(tasks);
      }
    });
  });
}

async function computeCompletedTasksByUser() {
  try {
    const tasks = await fetchTasks();

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
  } catch (error) {
    console.error('Error:', error.message);
  }
}

computeCompletedTasksByUser();
