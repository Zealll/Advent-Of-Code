const reader = require('fs')

reader.readFile('test.txt', (err, data) => {
    console.log(data.toString())
})