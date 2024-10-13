import { article_collumns } from "@/components/admin/article_columns";
import { Navbar } from "@/components/Navbar";
import { DataTableArticle } from "@/components/admin/article-table";
import { ColumnDef } from "@tanstack/react-table";
import { DataTableUser } from "@/components/admin/users-table";
import { userscolumns } from "@/components/admin/userscolumns";
import { DataTableGroups } from "@/components/admin/groups-table";
import { groupcolumns } from "@/components/admin/groupcolumns";
import { category_collumns } from "@/components/admin/categories-columns";
import { video_columns } from "@/components/admin/video_columns";
import { DataTableVideo } from "@/components/admin/video-table";
import { DataTableCategories } from "@/components/admin/categories-table";

async function getData() {
  const res = await fetch("http://127.0.0.1:8000/cms/dashboard/user");
    const data = await res.json();
    return data;
}

// async function getCSRFToken() {
//     console.log("csrf token being called")
//     const res = await fetch("http://localhost:8080/accounts/api/csrf", {
//         method: "GET",
//         credentials: "include",
//     });
//     const data = await res.json();
//     return data["csrfToken"];
// }

// async function getData() {
//     console.log("get data being called")
//     const token = await getCSRFToken();
//   const res = await fetch("http://127.0.0.1:8080/cms/dashboard/admin",
//     {
//       method: "GET",
//       credentials: "include",
//       headers: {
//         "X-CSRFToken": token,
//         "Content-Type": "application/json",
//       },
//     }
//   )
//   const data = await res.json()
//   return data
// }

export default async function AdminDashboard() {
    const data = await getData();
    const data_videos = data["videos"];
    const data_articles = data["articles"];
    const data_users = data["users"];
    const data_categories = data["categories"];
    const data_groups = data["groups"];

    return (
      <div className="container mx-auto py-10">
        <Navbar />
        <h1 className="text-5xl text-center font-bold">Administrator Dashboard</h1>
        <section>
        <h1 className="text-3xl font-semibold">Manage Videos</h1>
        <DataTableVideo columns={video_columns} data={data_videos} />
        </section>
        <section>
        <h1 className="text-3xl font-semibold">Mange Articles</h1>
        <DataTableArticle columns={article_collumns} data={data_articles} />
        </section>
        <section>
        <h1 className="text-3xl font-semibold">Mange Users</h1>
        <DataTableUser columns={userscolumns} data={data_users} />
        </section>
        <section>
        <h1 className="text-3xl font-semibold">Mange Categories</h1>
        <DataTableCategories columns={category_collumns} data={data_categories} />
        </section>
      </div>
    )
  }

