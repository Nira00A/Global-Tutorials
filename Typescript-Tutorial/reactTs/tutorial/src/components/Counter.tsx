import React, { useState } from 'react'

export default function Counter() {
    const [count , setCount] = useState<number | null>(0)

    return (
        <div>
            <p>Cups orderded: {count}</p>
            <button onClick={() => setCount((c)=>(c ?? 0)+1)}>
                Order one more
            </button>
        </div>
    )
}
