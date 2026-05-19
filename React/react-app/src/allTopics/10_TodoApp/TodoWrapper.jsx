import style from "./TodoWrapper.module.css"
import CreateTodo from "./CreateTodo/CreateTodo"
import DisplayTodo from "./DisplayTodo/DisplayTodo"
import { useState } from "react"

const TodoWrapper = () =>{
    const [todo, setTodo] = useState("")
    const [todoList, setTodoList] = useState(() => {
        let todos = JSON.parse(localStorage.getItem("todos")) || []
        return todos
    })
    const handleCreateTodo = (e) =>{
        e.preventDefault();
        let newTodo = {
            id: Date.now(),
            text: todo.trim()
        }
        console.log(newTodo);

        const todos = JSON.parse(localStorage.getItem("todos")) || []
        todos.push(newTodo)
        localStorage.setItem("todos", JSON.stringify(todos))

        setTodoList(todos)

        setTodo("")
    }

    return (
        <main className={style.wrapper}>
            <h1 className={style.heading}>
                Todo App
            </h1>
            <CreateTodo todo = {todo} setTodo = {setTodo} handleCreateTodo = {handleCreateTodo}/>
            <DisplayTodo todoList = {todoList}/>
        </main>
    )
}
export default TodoWrapper