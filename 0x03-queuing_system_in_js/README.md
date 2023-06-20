# 0x03. Queuing System in JS

![image](<https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/1/1486e02a78cdf7b4557c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230620%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230620T115338Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2671f702adafe464cf52e2fe170347ee3373fc597b4e8cdc893bbc3c0d72a28f>
)

## Resources

- [Redis quick start](https://redis.io/docs/getting-started/)
- [Redis client interface](https://redis.io/docs/ui/cli/)
- [Redis client for Node JS](https://github.com/redis/node-redis)
- [Kue](https://github.com/Automattic/kue) <i>deprecated but still use in the industry</i>

## Required Files for the Project

### package.json

    {
        "name": "queuing_system_in_js",
        "version": "1.0.0",
        "description": "",
        "main": "index.js",
        "scripts": {
          "lint": "./node_modules/.bin/eslint",
          "check-lint": "lint [0-9]*.js",
          "test": "./node_modules/.bin/mocha --require @babel/register --exit",
          "dev": "nodemon --exec babel-node --presets @babel/preset-env"
        },
        "author": "",
        "license": "ISC",
        "dependencies": {
          "chai-http": "^4.3.0",
          "express": "^4.17.1",
          "kue": "^0.11.6",
          "redis": "^2.8.0"
        },
        "devDependencies": {
          "@babel/cli": "^7.8.0",
          "@babel/core": "^7.8.0",
          "@babel/node": "^7.8.0",
          "@babel/preset-env": "^7.8.2",
          "@babel/register": "^7.8.0",
          "eslint": "^6.4.0",
          "eslint-config-airbnb-base": "^14.0.0",
          "eslint-plugin-import": "^2.18.2",
          "eslint-plugin-jest": "^22.17.0",
          "nodemon": "^2.0.2",
          "chai": "^4.2.0",
          "mocha": "^6.2.2",
          "request": "^2.88.0",
          "sinon": "^7.5.0"
        }
      }

## .babelrc

    {
      "presets": [
        "@babel/preset-env"
      ]
    }

### and…
Don’t forget to run <b>$ npm install</b> when you have the package.json

## Solutions for mandatory and advanced tasks...