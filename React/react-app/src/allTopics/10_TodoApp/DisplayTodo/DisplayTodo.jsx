import style from "./DisplayTodo.module.css"
const DisplayTodo = ({todoList}) =>{
    return (
        <div>
        <h1>Display Todo</h1>
        <ul className={style.todoList}>
            {
                todoList.map((todo) => {
                    return (
                            <li key={todo.id}>{todo.text}</li>
                    )
                })
            }
        </ul>
        </div>
    )
}

export default DisplayTodo;