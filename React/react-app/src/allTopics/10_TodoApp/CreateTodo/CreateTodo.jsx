import style from "./CreateTodo.module.css"
const CreateTodo = ({todo, setTodo, handleCreateTodo}) =>{
    return (
        <form className={style.todoform} onSubmit={handleCreateTodo}>
            <input type="text" name="todo" id="todo" value={todo} onChange={(e) => setTodo(e.target.value)} placeholder="Enter a Todo"/>
            <button>Add</button>
        </form>
    )
}

export default CreateTodo;