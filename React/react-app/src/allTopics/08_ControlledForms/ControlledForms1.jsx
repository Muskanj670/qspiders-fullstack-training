import { useState } from "react"

const ControlledForms1 = () => {
    const [username, setUsername] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [course, setCourse] = useState("")
    const [gender, setGender] = useState("")
    const [subjects, setSubjects] = useState([])
    const [age, setAge] = useState("")

    const handleUsername = (e) => setUsername(e.target.value)
    const handleEmail = (e) => setEmail(e.target.value)
    const handlePassword = (e) => setPassword(e.target.value)
    const handleCourse = (e) => setCourse(e.target.value)
    const handleGender = (e) => setGender(e.target.value)
    const handleSubjects = (e) => {
        const { value, checked } = e.target;
        if (checked) {
            setSubjects([...subjects, value]);
        } else {
            setSubjects(subjects.filter(subject => subject !== value));
        }
    }
    const handleAge = (e) => setAge(e.target.value)


    const handleSubmit = (e) => {
        e.preventDefault();
        console.log({ username, email, password, course, gender, subjects, age });
    }
    return (
        <>
            <h1>Learn Controlled Forms</h1>
            <form onSubmit={handleSubmit}>

                <label htmlFor="username">Username: </label>
                <input type="text" name="username" id="username" value={username} onChange={handleUsername} />
                <br />

                <label htmlFor="email">Email: </label>
                <input type="email" name="email" id="email" value={email} onChange={handleEmail} />
                <br />
                <label htmlFor="password">Password: </label>
                <input type="password" name="password" id="password" value={password} onChange={handlePassword} />
                <br />

                <label htmlFor="courses">Courses: </label>
                <select name="courses" id="courses" value={course} onChange={handleCourse}>
                    <option value="" disabled selected>Select Course</option>
                    <option value="Java Full Stack">Java Full Stack</option>
                    <option value="Python Full Stack">Python Full Stack</option>
                    <option value="MERN Full Stack">MERN Full Stack</option>
                </select>
                <br />

                <label htmlFor="gender">Gender: </label>
                <input type="radio" name="gender" id="genderMale" value="Male" checked={gender === "Male"} onChange={handleGender} />
                <label htmlFor="genderMale">Male</label>
                <input type="radio" name="gender" id="genderFemale" value="Female" checked={gender === "Female"} onChange={handleGender} />
                <label htmlFor="genderFemale">Female</label>
                <br />

                <label htmlFor="subjects">Subjects: </label>
                <input type="checkbox" name="subjects" id="subjectsPython" value="Python" checked={subjects.includes("Python")} onChange={handleSubjects} />
                <label htmlFor="subjectsPython">Python</label>
                <input type="checkbox" name="subjects" id="subjectsDjango" value="Django" checked={subjects.includes("Django")} onChange={handleSubjects} />
                <label htmlFor="subjectsDjango">Django</label>
                <input type="checkbox" name="subjects" id="subjectsReact" value="React" checked={subjects.includes("React")} onChange={handleSubjects} />
                <label htmlFor="subjectsReact">React</label>
                <br />

                <label htmlFor="age">Age: </label>
                <input type="number" name="age" id="age" value={age} onChange={handleAge} />
                <br />

                <button>Submit</button>
            </form >
        </>
    )
}

export default ControlledForms1