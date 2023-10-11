import React from 'react'

const TaskList = ({ todo, setTodo }) => {
    const clear = (task) => {
        setTodo(todo.filter((t)=> t !== task))
    }
  return (
      <div>
          {todo.map((task, index) => (
              <div key={index} className=' flex flex-auto gap-6 w-full mt-5 p-2 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700'>
                  <h2 className='text-2xl w-5/6 text-left mt-2'>{task}</h2>
                  <button type="button" className="w-1/6 text-white bg-gradient-to-r from-red-400 via-red-500 to-red-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-red-300 dark:focus:ring-red-800 shadow-lg shadow-red-500/50 dark:shadow-lg dark:shadow-red-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2" onClick={()=>clear(task)}>Clear</button>
              </div>
          ))}
    </div>
  )
}

export default TaskList