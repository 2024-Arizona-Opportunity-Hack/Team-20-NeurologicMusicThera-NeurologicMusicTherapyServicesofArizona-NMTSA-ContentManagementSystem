'use client';

import { useState, useEffect } from 'react';
import styles from './page.module.css';

export default function CreateArticle() {
  const [title, setTitle] = useState('');
  const [article, setArticle] = useState(null);
  const [accessGroups, setAccessGroups] = useState([]);
  const [thumbnail, setThumbnail] = useState(null);
  const [csrfToken, setCsrfToken] = useState('');

  useEffect(() => {
    fetchCsrfToken();
  }, []);

  const fetchCsrfToken = async () => {
    try {
      const response = await fetch('http://localhost:8000/accounts/api/csrf', {
        credentials: 'include',
      });
      const data = await response.json();
      setCsrfToken(data.csrfToken);
    } catch (error) {
      console.error('Error fetching CSRF token:', error);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append('title', title);
    formData.append('article', article);
    formData.append('access_groups', JSON.stringify(accessGroups));
    formData.append('thumbnail', thumbnail);

    try {
      const response = await fetch('http://localhost:8000/cms/dashboard/create/article', {
        method: 'POST',
        headers: {
          'X-CSRFToken': csrfToken,
        },
        body: formData,
        credentials: 'include',
      });

      if (response.ok) {
        console.log('Article created successfully');
        // Reset form or redirect user
      } else {
        console.error('Failed to create article');
      }
    } catch (error) {
      console.error('Error creating article:', error);
    }
  };

  const handleAccessGroupChange = (group) => {
    setAccessGroups((prevGroups) =>
      prevGroups.includes(group)
        ? prevGroups.filter((g) => g !== group)
        : [...prevGroups, group]
    );
  };

  return (
    <div className={styles.container}>
      <h1>Create Article</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="title">Title:</label>
          <input
            type="text"
            id="title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />
        </div>

        <div>
          <label htmlFor="article">Article:</label>
          <input
            type="file"
            id="article"
            onChange={(e) => setArticle(e.target.files[0])}
            required
          />
        </div>

        <div>
          <label>Access Groups:</label>
          <div>
            <label>
              <input
                type="checkbox"
                checked={accessGroups.includes('public')}
                onChange={() => handleAccessGroupChange('public')}
              />
              Public
            </label>
          </div>
          <div>
            <label>
              <input
                type="checkbox"
                checked={accessGroups.includes('consumers')}
                onChange={() => handleAccessGroupChange('consumers')}
              />
              Consumers
            </label>
          </div>
          <div>
            <label>
              <input
                type="checkbox"
                checked={accessGroups.includes('caregivers')}
                onChange={() => handleAccessGroupChange('caregivers')}
              />
              Caregivers
            </label>
          </div>
          <div>
            <label>
              <input
                type="checkbox"
                checked={accessGroups.includes('private')}
                onChange={() => handleAccessGroupChange('private')}
              />
              Private
            </label>
          </div>
          </div>
        </div>

        <div>
          <label htmlFor="thumbnail">Thumbnail:</label>
          <input
            type="file"
            id="thumbnail"
            accept="image/*"
            onChange={(e) => setThumbnail(e.target.files[0])}
            required
          />
        </div>

        <button type="submit">Create Article</button>
      </form>
    </div>
  );
}