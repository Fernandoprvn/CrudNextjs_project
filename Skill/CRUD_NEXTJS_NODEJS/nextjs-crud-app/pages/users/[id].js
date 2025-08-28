// pages/users/[id].js

import { useEffect, useState } from 'react';
import { useRouter } from 'next/router';
import axios from 'axios';
import styles from './Users.module.css';

export default function UserDetail() {
  const router = useRouter();
  const { id } = router.query;
  const [user, setUser] = useState(null);

  useEffect(() => {
    if (id) {
      axios.get(`http://localhost:4000/users/${id}`)
        .then(res => setUser(res.data))
        .catch(err => console.error(err));
    }
  }, [id]);

  if (!user) return <p className={styles.loading}>🌀 Loading user...</p>;

  return (
    <div className={styles.card}>
      <h1 className={styles.headingtitle}>{user.name}</h1>
      <p className={styles.paragraph}>📧 Email: {user.email}</p>
      <p className={styles.paragraph}>🆔 ID: {user._id}</p>
    </div>
  );
}
