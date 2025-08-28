import os
import zipfile

frontend_files = {
    "nextjs-crud-app/package.json": """\
{
  "name": "nextjs-crud-app",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  },
  "dependencies": {
    "axios": "^1.6.0",
    "next": "13.4.0",
    "react": "18.2.0",
    "react-dom": "18.2.0"
  }
}
""",
    "nextjs-crud-app/pages/index.js": """\
import Link from 'next/link';

export default function Home() {
  return (
    <div>
      <h1>Next.js CRUD App</h1>
      <Link href="/users">Go to Users</Link>
    </div>
  );
}
""",
    "nextjs-crud-app/pages/users/index.js": """\
import { useEffect, useState } from 'react';
import axios from 'axios';
import Link from 'next/link';

export default function UsersPage() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:3000/users')
      .then(res => setUsers(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h1>All Users</h1>
      <Link href="/users/create">Create New User</Link>
      <ul>
        {users.map(user => (
          <li key={user._id}>
            {user.name} - {user.email}
            <Link href={'/users/' + user._id}> View</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
""",
    "nextjs-crud-app/pages/users/create.js": """\
import { useState } from 'react';
import { useRouter } from 'next/router';
import axios from 'axios';

export default function CreateUser() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const router = useRouter();

  const handleSubmit = async (e) => {
    e.preventDefault();
    await axios.post('http://localhost:3000/users', { name, email });
    router.push('/users');
  };

  return (
    <div>
      <h1>Create User</h1>
      <form onSubmit={handleSubmit}>
        <input value={name} onChange={e => setName(e.target.value)} placeholder="Name" required />
        <input value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" required />
        <button type="submit">Create</button>
      </form>
    </div>
  );
}
""",
    "nextjs-crud-app/pages/users/[id].js": """\
import { useRouter } from 'next/router';
import { useEffect, useState } from 'react';
import axios from 'axios';

export default function UserDetail() {
  const router = useRouter();
  const { id } = router.query;
  const [user, setUser] = useState(null);

  useEffect(() => {
    if (id) {
      axios.get('http://localhost:3000/users/' + id)
        .then(res => setUser(res.data))
        .catch(err => console.error(err));
    }
  }, [id]);

  const deleteUser = async () => {
    await axios.delete('http://localhost:3000/users/' + id);
    router.push('/users');
  };

  return (
    <div>
      <h1>User Detail</h1>
      {user ? (
        <div>
          <p>Name: {user.name}</p>
          <p>Email: {user.email}</p>
          <button onClick={deleteUser}>Delete</button>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}
"""
}

zip_filename = "nextjs-crud-app.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for path, content in frontend_files.items():
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        zipf.write(path)

print(f"  Created: {zip_filename}")
