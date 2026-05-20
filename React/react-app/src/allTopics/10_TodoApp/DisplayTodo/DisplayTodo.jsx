import style from "./DisplayTodo.module.css"
const DisplayTodo = ({todoList, handleDeleteTodo, handleEditTodo}) =>{
    return (
        <div>
        <h1 id={style.DisplayTodo}>Display Todo</h1>
        {todoList.length === 0 ? <p>No Todo Available </p> : 
        <ul className={style.todoList}>
            {
                todoList.map((todo) => {
                    return (
                            <li key={todo.id}>
                                <span>{todo.text}</span>
                                <div>
                                    <button className={style.edit} onClick={() => handleEditTodo(todo.id)}>Edit</button> 
                                    <button className={style.del} onClick={() => handleDeleteTodo(todo.id)}>Delete</button>
                                </div>
                            </li>
                    )
                })
            }
        </ul>
        }
        </div>
    )
}

export default DisplayTodo;