import React, { useState } from "react";

function App() {
  const [token, setToken] = useState(localStorage.getItem("token") || "");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [editId, setEditId] = useState(null);

  const API_URL = "http://127.0.0.1:8000";

  const register = async () => {
    const res = await fetch(`${API_URL}/register`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });

    const data = await res.json();

    if (!res.ok) {
      alert(data.detail || "Registration failed");
      return;
    }

    alert("Registered successfully!");
  };

  const login = async () => {
    const res = await fetch(`${API_URL}/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });

    const data = await res.json();

    if (!res.ok) {
      alert(data.detail || "Login failed");
      return;
    }

    setToken(data.access_token);
    localStorage.setItem("token", data.access_token);
    alert("Logged in!");
  };

  const logout = () => {
    setToken("");
    localStorage.removeItem("token");

    setEmail("");
    setPassword("");
    setTasks([]);
    setTitle("");
    setDescription("");
    setEditId(null);

    alert("Logged out");
  };


  const fetchTasks = async () => {
    const res = await fetch(`${API_URL}/api/v1/tasks`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    const data = await res.json();

    if (!res.ok) {
      alert(data.detail || "Failed to load tasks");
      return;
    }

    setTasks(data);
  };

  const createTask = async () => {
    const res = await fetch(`${API_URL}/api/v1/tasks`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({ title, description }),
    });

    const data = await res.json();

    if (!res.ok) {
      alert(data.detail || "Task creation failed");
      return;
    }

    alert("Task created!");
    setTitle("");
    setDescription("");
    fetchTasks();
  };

  const updateTask = async () => {
    const res = await fetch(`${API_URL}/api/v1/tasks/${editId}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({ title, description }),
    });

    const data = await res.json();

    if (!res.ok) {
      alert(data.detail || "Update failed");
      return;
    }

    alert("Task updated!");
    setEditId(null);
    setTitle("");
    setDescription("");
    fetchTasks();
  };

  const deleteTask = async (id) => {
    const res = await fetch(`${API_URL}/api/v1/tasks/${id}`, {
      method: "DELETE",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    const data = await res.json();

    if (!res.ok) {
      alert(data.detail || "Delete failed");
      return;
    }

    alert("Task deleted!");
    fetchTasks();
  };

  return (
    <div
      style={{
        maxWidth: 500,
        margin: "40px auto",
        padding: 25,
        border: "1px solid #ddd",
        borderRadius: 10,
        fontFamily: "Arial",
        backgroundColor: "#f9f9f9",
        boxShadow: "0 4px 8px rgba(0,0,0,0.1)",
      }}
    >
      <h2 style={{ textAlign: "center" }}>FastAPI + React Task Manager</h2>

      <h3>Register / Login</h3>
      <input
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        style={{
          width: "100%",
          padding: 8,
          marginBottom: 10,
          borderRadius: 4,
          border: "1px solid #ccc",
        }}
      />

      <input
        placeholder="Password"
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        style={{
          width: "100%",
          padding: 8,
          marginBottom: 10,
          borderRadius: 4,
          border: "1px solid #ccc",
        }}
      />

      <div style={{ marginBottom: 15 }}>
        <button
          style={{ marginRight: 8 }}
          onClick={register}
        >
          Register
        </button>

        <button
          style={{ marginRight: 8 }}
          onClick={login}
        >
          Login
        </button>

        <button onClick={logout}>Logout</button>
      </div>

      <h3>Tasks</h3>
      <button onClick={fetchTasks}>Load Tasks</button>

      <ul style={{ paddingLeft: 20 }}>
        {tasks.map((task) => (
          <li key={task.id} style={{ marginBottom: 8 }}>
            <strong>{task.title}</strong> – {task.description}

            <div style={{ marginTop: 5 }}>
              <button
                style={{ marginRight: 6 }}
                onClick={() => {
                  setEditId(task.id);
                  setTitle(task.title);
                  setDescription(task.description);
                }}
              >
                Edit
              </button>

              <button onClick={() => deleteTask(task.id)}>
                Delete
              </button>
            </div>
          </li>
        ))}
      </ul>

      <h3>{editId ? "Update Task" : "Create Task"}</h3>

      <input
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        style={{
          width: "100%",
          padding: 8,
          marginBottom: 10,
          borderRadius: 4,
          border: "1px solid #ccc",
        }}
      />

      <input
        placeholder="Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        style={{
          width: "100%",
          padding: 8,
          marginBottom: 10,
          borderRadius: 4,
          border: "1px solid #ccc",
        }}
      />

      {editId ? (
        <button onClick={updateTask}>
          Update Task
        </button>
      ) : (
        <button onClick={createTask}>
          Create Task
        </button>
      )}
    </div>
  );
  ;
}

export default App;
