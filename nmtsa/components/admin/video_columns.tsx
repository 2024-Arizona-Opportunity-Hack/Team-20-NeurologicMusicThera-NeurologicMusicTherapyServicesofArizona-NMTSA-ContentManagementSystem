import { ColumnDef } from "@tanstack/react-table";

export type Video = {
    title: string;
    category: string;
    tags: string;
    date: string;
    path: string;
    thumbnail: string;
    id: string;
    access_groups: Array<string>;
};

export const video_columns: Array<ColumnDef<Video>> = [
    {
        header: "Title",
        accessorKey: "title",
    },
    {
        header: "Category",
        accessorKey: "category",
    },
    {
        header: "tags",
        accessorKey: "tags",
    },
    {
        header: "Date",
        accessorKey: "date",
    },
    {
        header: "Path",
        accessorKey: "path",
    },
    {
        header: "File",
        accessorKey: "file",
    },
    {
        header: "Access Groups",
        accessorKey: "access_groups",
    },
];

