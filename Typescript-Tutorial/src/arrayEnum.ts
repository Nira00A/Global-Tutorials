const chaiFlavours: string[] = ["masala" , "adrak"]
const chaiPrice: number[] = [10.20]

const rating: Array<number> = [1,4.5,2.2]

type chai = {
    name: string,
    price: number
}

const menu: chai[] = [
    {name: 'Masala' , price: 15},
    {name: 'Adrak' , price: 20}
]

// read only

const cities: readonly string[] = ["Delhi" , "Jaipur"]
// cities.push("pune") // error

// multi dimentional array

const table: number[][] = [
    [1,2,3],
    [2,3,5]
]

let chaiTupple: [string , number]

chaiTupple = ["string" , 20]

// chaiTupple = [20 , "masala"] // order also matters

let userInfo: [string , number , boolean?]

userInfo=[
    "Arin",
    100,
    true
]

// read only tupple

const location: readonly [number , number] = [22,44]


// named tupple

const chaiItems: [name: string , price: number] = ["Masala" , 25]

// enums

enum CupSize {
    small ,
    medium,
    large
}

const size = CupSize.large // .large , .small

enum Status {
    PENDING = 100,
    SERVED, // 101
    CANCELLED //102
}

enum ChaiType {
    MASALA = "masala",
    GINGER = "ginger",
}

function makeChai(type: ChaiType){
    console.log(`Making: ${type}`)
}

makeChai(ChaiType.GINGER)
// makeChai('masala')  // will give error

// Heterogeneous Values

enum RandomEnum { // All numbers or all string or all empty but not heterogeneous
    ID = 1,
    NAME = 'chai'
}

const enum Sugar {
    LOW = 1,
    MEDIUM = 2,
    HIGH = 3
}

const s = Sugar.HIGH // Normal but very rare practice


