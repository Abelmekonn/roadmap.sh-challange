#!/usr/bin/env node
const axios = require('axios');
const { program } = require('commander');
const chalk = require('chalk');

const BASE_URL = 'https://api.github.com/users/';

program
    .version('1.0.0')
    .description('GitHub User Activity CLI Tool')
    .argument('<username>', 'GitHub username')
    .action(async (username) => {
        try {
            const { data } = await axios.get(`${BASE_URL}${username}`);
            console.log(chalk.green(`User: ${data.name}`));
            console.log(`Bio: ${data.bio}`);
            console.log(`Location: ${data.location}`);
            console.log(`Public Repos: ${data.public_repos}`);
            console.log(`Followers: ${data.followers}`);
            console.log(`Following: ${data.following}`);
        } catch (error) {
            console.error(chalk.red('Error fetching user data.'));
        }
    });

program
    .command('repos')
    .description('List user repositories')
    .action(async (username) => {
        try {
            const { data } = await axios.get(`${BASE_URL}${username}/repos`);
            data.forEach(repo => {
                console.log(chalk.blue(`Repo: ${repo.name}`));
                console.log(`Stars: ${repo.stargazers_count}, Forks: ${repo.forks_count}`);
                console.log(`Language: ${repo.language}`);
                console.log('---');
            });
        } catch (error) {
            console.error(chalk.red('Error fetching repositories.'));
        }
    });

program.parse(process.argv);
