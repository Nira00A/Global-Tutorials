interface Chai {
    flavour: string,
    price: number
}

const masala:Chai = {
    flavour: 'masala',
    price: 30
}

// methods using interface

interface TeaMachine{
    start(): void
    stop(): void
}

const machine: TeaMachine = {
    start(){
        console.log()
    },
    stop(){

    }
}

// index signature

interface ChaiRating {
    [flavor: string]: number
}

const ratings: ChaiRating = {
    masala: 4.5,
    ginger: 5   
}

// double interfaces

interface User {
    name: string
}

interface User {
    age: number
}

const u: User = {
    name: 'Arin',
    age: 12
}

//Merging syntax
 
interface A {
    a : string
}

interface B {
    b: string
}

interface u1 extends A , B{

} 

// Generics

function wrapInArray<T>(item: T): T[]{
    return [item]
}

wrapInArray("Masala")
wrapInArray(34)
wrapInArray({flavor: "Ginger0"})

function pair<A , B>(a: A, b: B): [A,B]{
    return [a, b]
}

// usage of Generics

pair("masala" , "test")
pair("masala" , 30)

// generic interface

interface Box<T>{
    content: T
}

const numberBox: Box<number> = {
    content: 10
}

const numberBox2: Box<string> = {
    content: "10"
}

// generic usecase 

interface ApiPromise<T>{
    status: number,
    data: T
}

const res: ApiPromise<{flavor: string}> = {
    status: 200,
    data: {flavor: 'masala'}
}