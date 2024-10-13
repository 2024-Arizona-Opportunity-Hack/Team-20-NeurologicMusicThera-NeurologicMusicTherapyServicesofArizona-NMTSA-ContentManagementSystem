import { Video, columns } from "@/components/admin/columns";
import { DataTable } from "@/components/admin/data-table";
import { Navbar } from "@/components/Navbar";

async function getVideos() {
  return [
    {
      title: "The History of JavaScript",
      transcript: "A transcript of the video",
      category: "JavaScript",
      tags: ["JavaScript", "History"],
      date: "2021-10-01",
      file: "https://example.com/video.mp4",
    access: "Public",
    },
    {
        title: "The History of JavaScript",
        transcript: "A transcript of the video",
        category: "JavaScript",
        tags: ["JavaScript", "History"],
        date: "2021-10-01",
        file: "https://example.com/video.mp4",
      access: "Public",
      }
  ]
}

export default async function AdminDashboard() {
    const data = await getVideos()
   
    return (
      <div className="container mx-auto py-10">
        <Navbar />
        <DataTable columns={columns} data={data} />
      </div>
    )
  }

