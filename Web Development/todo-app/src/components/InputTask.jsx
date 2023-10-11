import React,{useState} from 'react'

const InputTask = ({ todo, setTodo }) => {
    const [task, setTask] = useState('')
  const addTask = () => {
    if (task) {
        setTodo([...todo, task])
        setTask('')
      }
    }
  return (
      <div className='flex flex-auto gap-6'>
        <input type="text" className="w-5/6 py-3 px-5 border-black-100 rounded-full" placeholder="Add task..." onChange={(e)=>setTask(e.target.value)}></input>
        <button type="button" className="w-1/6 py-3 px-4 inline-flex justify-center items-center gap-2 rounded-md bg-green-100 border border-transparent font-semibold text-green-500 hover:text-white hover:bg-green-100 focus:outline-none focus:ring-2 ring-offset-white focus:ring-green-500 focus:ring-offset-2 transition-all text-sm dark:focus:ring-offset-gray-800" onClick={addTask}>Add Task</button>
      </div>
  )
}

export default InputTask