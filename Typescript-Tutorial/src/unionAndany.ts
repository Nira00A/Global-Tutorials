let subs: number | string = '1M'

let apiRequestStatus: 'pending' | 'success' | 'error' = 'pending'   

// apiRequestStatus = 'Arin' error

apiRequestStatus = "success"

const orders = ['12' , '33' , '55']

let currentOrder: string | undefined // undefined removed then error (Ts)

for (let order in orders){
    if(order === "12"){
        currentOrder = order
        break
    }
}

console.log(currentOrder)