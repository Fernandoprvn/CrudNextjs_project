// pages/users/create.js

import { useState } from 'react';
import axios from 'axios';
import { useRouter } from 'next/router';
import styles from './Users.module.css'

export default function CreateUser() {
  const router = useRouter();
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    await axios.post('http://localhost:4000/users', { name, email });
    router.push('/users');
  };

  return (
    <div className={styles.container2}>
      <h1 className={styles.heading}>🧙‍♂️ Create a Magical User</h1>
      <form onSubmit={handleSubmit} className={styles.form}>
        <label>Name</label>
        <input
        className={styles.inputbox}
          type="text"
          required
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <label>Email</label>
        <input
        className={styles.inputbox}
          type="email"
          required
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <button type="submit" className={styles.btnCont}>✨ Add User</button>
      </form>
    </div>
  );
}
