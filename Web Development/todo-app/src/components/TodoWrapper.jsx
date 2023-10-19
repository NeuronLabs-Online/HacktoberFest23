import React, {useState} from 'react'
import InputTask from './InputTask'
import TaskList from './TaskList'
// import mycomponent from './mycomponent'


const TodoWrapper = () => {
    const [todo, setTodo] = useState([])
    return (
      <>
    <div>
        <h1 className='font-mono text-5xl antialiased font-semibold'>TODO APP</h1>   
        <br></br>   
    </div>
    <div>
                <InputTask todo={todo} setTodo={setTodo} />
                <TaskList todo={todo} setTodo={setTodo} />
                
    </div>
     </>
  )
}

export default TodoWrapper