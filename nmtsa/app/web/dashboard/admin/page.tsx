<<<<<<< HEAD
import { Video, columns } from "@/components/admin/columns";
import { articlecolumns } from "@/components/admin/articlecolumns";
import { DataTable } from "@/components/admin/data-table";
import { Navbar } from "@/components/Navbar";
import DataTableArticles from "@/components/admin/TableArticles";
import { ColumnDef } from "@tanstack/react-table";
import { DataTableUsers } from "@/components/admin/TableUsers";
import { userscolumns } from "@/components/admin/userscolumns";
import { DataTableGroups } from "@/components/admin/TableGroups";
import { groupcolumns } from "@/components/admin/groupcolumns";

async function getData() {
  const res = await fetch("http://127.0.0.1:8080/cms/dashboard/admin");
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

=======
import { Video, video_columns } from "@/components/admin/video_columns";
import { article_collumns } from "@/components/admin/article_columns";
import { Navbar } from "@/components/Navbar";
import { DataTableArticle } from "@/components/admin/article-table";
import { DataTableCategories } from "@/components/admin/categories-table";
import { DataTableVideo } from "@/components/admin/video-table";
import { DataTableGroups } from "@/components/admin/groups-table";
import { group_columns } from "@/components/admin/groups_columns";
import { category_collumns } from "@/components/admin/categories-columns";
import { user_columns } from "@/components/admin/users_columns";
import { DataTableUser } from "@/components/admin/users-table";
import { ColumnDef } from "@tanstack/react-table";

async function getData() {
  const res = await fetch("http://localhost:8000/cms/dashboard/admin");
  const data = await res.json();
  return data;
}

>>>>>>> frontend-copy
export default async function AdminDashboard() {
    const data = await getData();
    const data_videos = data["videos"];
    const data_articles = data["articles"];
<<<<<<< HEAD
    const data_groups = data["groups"];
    const data_users = data["users"];
    console.log(data)
=======
    const data_users = data["users"];
    const data_categories = data["categories"];
    const data_groups = data["groups"];
>>>>>>> frontend-copy

    return (
      <div className="container mx-auto py-10">
        <Navbar />
        <h1 className="text-5xl text-center font-bold">Administrator Dashboard</h1>
        <section>
<<<<<<< HEAD
        <h1 className="text-3xl font-semibold">Mange Videos</h1>
        <DataTable columns={columns} data={data_videos} />
        </section>
        <section>
        <h1 className="text-3xl font-semibold">Mange Articles</h1>
        <DataTableArticles columns={articlecolumns} data={data_articles} />
        </section>
        <section>
        <h1 className="text-3xl font-semibold">Manage Users</h1>
        <DataTableUsers columns={userscolumns} data={data_users} />
        </section>
        <section>
        <h1 className="text-3xl font-semibold">Manage Groups</h1>
        <DataTableGroups columns={groupcolumns} data={data_groups} />
        </section>
      </div>
    )
  }
=======
        <h1 className="text-3xl font-semibold">Manage Videos</h1>
        <DataTableVideo columns={video_columns} data={data_videos} />
        </section>
        <section>
        <h1 className="text-3xl font-semibold">Mange Articles</h1>
        <DataTableArticle columns={article_collumns} data={data_articles} />
        </section>
        <section>
        <h1 className="text-3xl font-semibold">Mange Users</h1>
        <DataTableUser columns={user_columns} data={data_users} />
        </section>
        <section>
        <h1 className="text-3xl font-semibold">Mange Categories</h1>
        <DataTableCategories columns={category_collumns} data={data_categories} />
        </section>
      </div>
    )
  }

>>>>>>> frontend-copy
