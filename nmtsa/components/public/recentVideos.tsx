import HeroVideoDialog from "@/components/ui/hero-video-dialog";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { getCsrfToken } from "@/app/utils/sendcsrf";


async function fetchTopVideos() {

  const response = await fetch("http://127.0.0.1:8000/",{
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken,
    },
    credentials: 'include',  
});
console.log(response)
  return response;
}

export async function RecentVideos() {
  const videos = await fetchTopVideos();
    return (
        <main>
            <h1 className="text-3xl font-semibold">Public Videos</h1>
        <div className="flex space-x-8">
      </div>
      </main>
    );
  }