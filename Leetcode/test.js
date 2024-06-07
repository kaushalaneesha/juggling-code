function calculate(arr, msg){
    arr[1] = 150
    msg = "inside"
    console.log(arr[0] + arr[1])
    console.log(msg)
}

const arr = [100]
let msg = "outside"

calculate(arr, msg)

console.log(arr[0] + arr[1])
console.log(msg)

const x = {}
x['foo'] = 'bar'
x.bar = {
    'first':100,
    'second': 200
}

console.log(x.bar['first']  + x['bar'].second)