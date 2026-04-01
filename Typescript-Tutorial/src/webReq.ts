import axios from 'axios'
import type { AxiosResponse } from 'axios'

interface Todo {
    userId : number,
    id: number,
    title: string,
    completed: boolean
}
 
const fetchData = async () => {
    try {
        const response: AxiosResponse<Todo> = await axios.get("https://rest")
        console.log("Todo" , response.data)
    } catch (error: any) {
        if(axios.isAxiosError(error)){
            console.log(error.message)
        }
    }
}
