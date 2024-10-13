import { Video, columns } from "@/components/admin/columns";
import { articlecolumns } from "@/components/admin/articlecolumns";
import { DataTable } from "@/components/admin/data-table";
import { Navbar } from "@/components/Navbar";
import { DataTableArticles } from "@/components/admin/TableArticles";
import { ColumnDef } from "@tanstack/react-table";
import { getCSRFToken } from "@/components/csrf_handling";

async function getVideos() {

    const token = await getCSRFToken();
  const res = await fetch("http://127.0.0.1:8000/cms/dashboard/admin",
    {
      method: "GET",
      credentials: "include",
      headers: {
        "X-CSRFToken": token,
        "Content-Type": "application/json",
      },
    }
  )
  const data = await res.json()
  return data["videos"]
}

async function getArticles() {
    const token = await getCSRFToken();
  const res = await fetch("http://127.0.0.1:8000/cms/dashboard/admin",
    {
      method: "GET",
      credentials: "include",
      headers: {
        "X-CSRFToken": token,
        "Content-Type": "application/json",
      },
    }
  )
  const data = await res.json()
  return data["articles"]
}

export default async function AdminDashboard() {
    const data_videos = await getVideos()
   const data_articles = await getArticles()

    return (
      <div className="container mx-auto py-10">
        <Navbar />
        <h1 className="text-5xl text-center font-bold">Private Dashboard</h1>
        <section>
        <h1 className="text-3xl font-semibold">Mange Videos</h1>
        <DataTable columns={columns} data={data_videos} />
        </section>
        <section>
        <h1 className="text-3xl font-semibold">Mange Articles</h1>
        <DataTableArticles columns={articlecolumns as ColumnDef<{ title: string; category: string; tags: string[]; date: string; file: string; access: string; }, unknown>[]} data={data_articles} />
        </section>
      </div>
    )
  }