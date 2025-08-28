// pages/users/index.js

import { useEffect, useState } from 'react';
import axios from 'axios';
import Link from 'next/link';
import styles from './Users.module.css'; // Import CSS module

export default function UsersPage() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:4000/users') // Adjust backend URL if needed
      .then(res => {
        setUsers(res.data);
      })
      .catch(err => {
        console.error('Failed to fetch users:', err.message);
      });
  }, []);

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>All Users</h1>
      <Link href="/users/create" className={styles.createBtn}>
        ➕ Create New User
      </Link>

      {users.length === 0 ? (
        <p>No users found.</p>
      ) : (
        <table className={styles.userTable}>
          <thead>
            <tr>
              <th>Name</th>
              <th>Email</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {users.map(user => (
              <tr key={user._id}>
                <td>{user.name}</td>
                <td>{user.email}</td>
                <td>
                  <Link href={`/users/${user._id}`} className={styles.viewBtn}>View</Link>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
