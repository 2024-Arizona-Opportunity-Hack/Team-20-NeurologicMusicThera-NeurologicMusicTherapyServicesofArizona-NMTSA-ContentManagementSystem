import { Navbar } from "@/components/Navbar";
import { TableVideos } from "@/components/admin/TableVideos";

export default function AdminDashboard() {
    const videos = [
        {
            title: 'Video 1',
            tags: ['tag1', 'tag2'],
            filepath: '/path/to/video1.mp4',
            category: 'Category 1',
            transcript: 'This is the transcript for video 1',
            accessGroup: 'Group 1',
        },
        {
            title: 'Video 2',
            tags: ['tag3', 'tag4'],
            filepath: '/path/to/video2.mp4',
            category: 'Category 2',
            transcript: 'This is the transcript for video 2',
            accessGroup: 'Group 2',
        },
        {
            title: 'Video 3',
            tags: ['tag5', 'tag6'],
            filepath: '/path/to/video3.mp4',
            category: 'Category 3',
            transcript: 'This is the transcript for video 3',
            accessGroup: 'Group 3',
        },
    ];

    return (
        <main>
        <Navbar></Navbar>
        <TableVideos></TableVideos>
        </main>
    );
}