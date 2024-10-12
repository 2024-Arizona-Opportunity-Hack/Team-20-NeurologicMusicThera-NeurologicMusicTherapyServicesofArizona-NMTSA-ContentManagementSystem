import { Navbar } from "@/components/Navbar";
import { TableVideos } from "@/components/admin/TableVideos";

export default function AdminDashboard() {
    const arrayofvids = [
        {
            title: "test",
            filePath: "https://example",
            transcript: "This is a transcript",
            group: "Admin",
            category: "Admin",
            tags: ["Admin", "test"]
        }
    ]
    return (
        <main>
        <Navbar></Navbar>
        <TableVideos name="videos" list={arrayofvids}></TableVideos>
        </main>
    );
}