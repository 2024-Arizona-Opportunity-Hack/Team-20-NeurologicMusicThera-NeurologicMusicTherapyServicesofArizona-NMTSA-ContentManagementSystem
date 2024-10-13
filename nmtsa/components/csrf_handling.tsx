export async function getCSRFToken() {
    const res = await fetch("http://localhost:8000/accounts/api/csrf", {
        method: "GET",
        credentials: "include",
    });
    const data = await res.json();
    return data["csrfToken"];
}