const chai = {
    name: 'Masala chai',
    price: 20,
    isHot: true
}

//Declaring object types

let tea : {
    name: string,
    price: number,
    isHot: Boolean
}

tea = {
    name: 'Ginger',
    price : 12,
    isHot: true
}

type Tea = {
    name: string,
    price: number,
    ingredients: string[]
}

const adrakChai: Tea = {
    name: "Chai garam",
    price: 12,
    ingredients: ["kaka" , "kuku"]
}

type Cup = {
    size: string
}

let smallCup : Cup = {size: "200ml"}
let bigCup = {size: "500ml", material: "steel"}

smallCup = bigCup // no issue in ading new objects

let small = {name : "smol"}
let big = {name : "big" , size: 10}

small = big

//Main type problem

type User = {
    username: string,
    pass : string
}

const u1: User = {
    username: 'Chai',
    pass: 'Code',
} 

type Chai = {
    name: string,
    price: number,
    isHot: boolean
}

const updateChai = (data: Partial<Chai>) => {  // Partial have all the values optional
    console.log('Updating chai' , data)
}

updateChai({}) // we can pass empty object too
updateChai({price: 10})
updateChai({isHot: true})

const updateChai2 = (data: Required<Chai>) => {  // Required need all the values required
    console.log('Updating chai' , data)
}

updateChai2({
    name: "Chai",
    price: 10,
    isHot: true
})

type Chai2 = {
    name: string,
    price: number,
    isHot: boolean,
    ingre : string[]
}

type  BasicChaiInfo = Pick<Chai2 , "name" | "price"> // Pick the values you need no less but can take more

const chaiInfo : BasicChaiInfo = {
    name: "Lemon Tea",
    price: 12
}

type Chai3 = {
    name: string,
    price: number,
    isHot: boolean,
    ingre : string[],
    secretIngre: string
}

type PublicChai = Omit<Chai3 , "secretIngre"> 

const chaiInfo2 : PublicChai = {
    name: 'Chai',
    price: 12,
    isHot: true,
    ingre: ["leaves" , "sugar"],
    // secretIngre: (this will not be included)
}

