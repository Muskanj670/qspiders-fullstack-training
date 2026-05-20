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

    const [editTodoId, seteditTodoId] = useState(null)
    const handleCreateTodo = (e) =>{
        e.preventDefault();

        if(editTodoId){
            const UpdateTodo = todoList.map((ele) => {
                if(ele.id === editTodoId){
                    return {...ele, text: todo.trim()}
                }
                return ele
            })

            setTodoList(UpdateTodo)
            localStorage.setItem("todos", JSON.stringify(UpdateTodo))
            setTodo("")
            seteditTodoId(null)
            return
        }

        let newTodo = {
            id: Date.now(),
            text: todo.trim()
        }

        const todos = JSON.parse(localStorage.getItem("todos")) || []
        todos.push(newTodo)
        localStorage.setItem("todos", JSON.stringify(todos))
        setTodoList(todos)
        setTodo("")
    }

    const handleDeleteTodo = (id) =>{
        let todos = [...todoList]
        let filteredTodos = todos.filter((ele) => ele.id !== id)
        setTodoList(filteredTodos)
        localStorage.setItem("todos",JSON.stringify(filteredTodos))
    }

    const handleEditTodo = (id) =>{
        const todos = [...todoList]
        const todoToBeEdit = todos.find(ele => ele.id === id)
        setTodo(todoToBeEdit.text)
        seteditTodoId(id)

    }

    return (
        <main className={style.wrapper}>
            <h1 className={style.heading}>
                Todo App
            </h1>
            <CreateTodo todo = {todo} setTodo = {setTodo} handleCreateTodo = {handleCreateTodo} editTodoId = {editTodoId}/>
            <DisplayTodo todoList = {todoList} handleDeleteTodo = {handleDeleteTodo} handleEditTodo = {handleEditTodo}/>
        </main>
    )
}
export default TodoWrapper