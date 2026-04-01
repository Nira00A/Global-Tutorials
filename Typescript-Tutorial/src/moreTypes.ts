let response: any = "any"

console.log(response.length)

let numericLenght: number = (response as string).length

type Book = {
    name: string
}

let bookString = '{"name" : "who moved my cheese"}'
let bookObject = JSON.parse(bookString) as Book

console.log(bookObject)

const inputElement = document.getElementById('username') as HTMLInputElement

// Any
let value: any

value = 'chai'
value = [1,2,3]
value = 2.5
value.toUpperCase()

let newValue: unknown

newValue = 'chai'
newValue = [1,2,3]
newValue = 2.5
// error given newValue.toUpperCase() 
if(typeof newValue === 'string'){
    newValue.toUpperCase()
}

 // try catch

 try {
    
 } catch (error) {
    if(error instanceof Error){
        console.log(error.message)
    }

    console.log("error" , error)
 }

const data: unknown = 'adwdw'
const strData: string = data as string

type Role = "admin" | "user" // | "superadmin" then role becomes superadmin from never datatype

function redirect(role:Role) : void {
    if (role = "admin"){
        console.log('Admin')
        return
    } 
    if (role = "user"){
        console.log('User')
        return
    } 
    role // this is now never data type
}

