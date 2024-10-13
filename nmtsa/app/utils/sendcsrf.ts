export async function getCsrfToken() {
    const response = await fetch('http://localhost:8000/accounts/api/csrf', {
      credentials: 'include',
    });
    const data = await response.json();
    return data.csrfToken;
  }